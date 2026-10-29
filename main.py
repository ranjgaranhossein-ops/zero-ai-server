from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ZERO AI")

class ChatRequest(BaseModel):
message: str

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
"chat": False,
"web_search": False,
"image_generation": False
}

@app.post("/chat")
@app.post("/api/chat")
def chat(request: ChatRequest):
return {
"reply": "ZERO AI server is running, but an AI API key is not configured yet."
}
