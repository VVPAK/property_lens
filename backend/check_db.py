import asyncio
from app.core.database import AsyncSessionLocal
from sqlalchemy import text

async def check_db():
    try:
        async with AsyncSessionLocal() as session:
            res = await session.execute(text('SELECT 1'))
            print(f'DB Check Success: {res.scalar()}')
    except Exception as e:
        print(f"DB Check Failed: {e}")

if __name__ == "__main__":
    asyncio.run(check_db())
