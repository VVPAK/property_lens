from fastapi import APIRouter, HTTPException, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent.service import agent_service
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    try:
        response_text = await agent_service.chat(request.message)
        return ChatResponse(response=response_text)
    except Exception as e:
        logger.error(f"Agent error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
