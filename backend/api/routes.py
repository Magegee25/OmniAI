from fastapi import APIRouter

from backend.api.models import ChatRequest, ChatResponse
from backend.llm.ollama import OllamaLLM

router = APIRouter()
ollama = OllamaLLM()


@router.get("/")
def root():
    return {
        "message": "Welcome to OmniAI!"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = ollama.chat(request.message)

    return ChatResponse(
        success=True,
        reply=response
    )