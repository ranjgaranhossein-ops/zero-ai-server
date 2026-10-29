import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ZERO AI Server")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


class ChatRequest(BaseModel):
    message: str
    history: list = []


@app.get("/")
def home():
    return {
        "name": "ZERO AI",
        "status": "online",
        "message": "Welcome to ZERO AI!"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/capabilities")
def capabilities():
    return {
        "chat": True,
        "history": True,
        "web_search": False,
        "image_generation": False
    }


@app.post("/chat")
@app.post("/api/chat")
async def chat(request: ChatRequest):
    if not API_KEY:
        raise HTTPException(
            status_code=503,
            detail="GEMINI_API_KEY is not configured."
        )

    contents = []

    for item in request.history:
        if isinstance(item, dict):
            role = item.get("role", "user")
            text = item.get("content", item.get("text", ""))

            if role == "assistant":
                role = "model"
            elif role != "model":
                role = "user"

            if text:
                contents.append({
                    "role": role,
                    "parts": [{"text": str(text)}]
                })

    contents.append({
        "role": "user",
        "parts": [{"text": request.message}]
    })

    url = (
        "https://generativelanguage.googleapis.com/"
        f"v1beta/models/{MODEL}:generateContent"
    )

    async
