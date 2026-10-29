from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline

MODEL_NAME = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"

app = FastAPI(
    title="Sentiment API",
    description="API de análise de sentimento com modelo do Hugging Face",
    version="1.0.0",
)

# Carrega o modelo uma vez, na inicialização
classifier = pipeline("text-classification", model=MODEL_NAME)


class TextInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)


class Prediction(BaseModel):
    label: str
    score: float


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL_NAME}


@app.post("/predict", response_model=Prediction)
def predict(payload: TextInput):
    result = classifier(payload.text, truncation=True)[0]
    return Prediction(label=result["label"], score=round(result["score"], 4))