# database/db.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# Create an async engine using asyncpg
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory for AsyncSession
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Dependency to be used in FastAPI endpoints
async def get_db():
    async with async_session() as session:
        yield session
