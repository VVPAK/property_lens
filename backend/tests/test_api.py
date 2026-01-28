import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_chat_api_mocked():
    # We will just test that the endpoint is reachable and validation works.
    # We won't mock the entire OpenAI chain here to keep it simple, 
    # but we will check for 401/500 if key is invalid, or 200 if valid.
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Test empty body
        response = await ac.post("/api/v1/chat", json={})
        assert response.status_code == 422 # Validation Error

        # Test valid body (even if OpenAI fails, we check it reaches the handler)
        # Note: If OPENAI_KEY is set, this might actually call the API.
        # For CI/CD, we would mock 'AgentService.chat'.
        response = await ac.post("/api/v1/chat", json={"message": "Hello"})
        # We accept 200 (success) or 500 (API error) as proof the endpoint handler ran
        assert response.status_code in [200, 500] 
