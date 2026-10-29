# Sentiment API

API REST para análise de sentimento em texto (multilíngue, incluindo português), construída com FastAPI e um modelo do Hugging Face.

## Modelo
[lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)

## Endpoints
| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Status da API |
| POST | `/predict` | Retorna o sentimento de um texto |

## Como rodar
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Documentação interativa em `http://127.0.0.1:8000/docs`.

## Exemplo
Requisição:
```json
{"text": "Adorei o atendimento, super recomendo!"}
```
Resposta:
```json
{"label": "positive", "score": 0.97}
```

![Swagger UI](docs.png)

## Stack
Python, FastAPI, Transformers (Hugging Face), PyTorch

## Próximos passos
- Deploy no Hugging Face Spaces
- Interface web com Gradio
- Dockerfile