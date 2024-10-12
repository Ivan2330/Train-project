from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from fastapi_users.db import SQLAlchemyUserDatabase
from typing import AsyncGenerator
from fastapi import Depends
from app.models import User, Base
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    expire_token_minutes: int = 30
    
    log_level: str = "info"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()

engine = create_async_engine(settings.database_url, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
    
