from fastapi import APIRouter

from backend.api.models import ChatRequest, ChatResponse
from backend.llm.fake import FakeLLM

router = APIRouter()
llm = FakeLLM()


@router.get("/")
def root():
    return {
        "message": "Welcome to OmniAI!"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = llm.chat(request.message)

    return ChatResponse(
        success=True,
        reply=response
    )