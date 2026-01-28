from fastapi import APIRouter, HTTPException, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent.service import agent_service
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

from fastapi.responses import StreamingResponse

@router.post("/chat")
async def chat_with_agent(request: ChatRequest):
    return StreamingResponse(
        agent_service.chat_stream(request.message),
        media_type="text/event-stream"
    )
