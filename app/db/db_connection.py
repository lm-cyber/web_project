from typing import Generator, AsyncGenerator

from fast_autocomplete import AutoComplete
from sqlalchemy import Engine, inspect, text
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker

from shema.base import Base


from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tablews():
    async with engine.begin() as conn:
        if not engine.dialect.has_table(engine, "users"):
            await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def init_models():
    async with engine.begin() as conn:
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS pg_trgm;"))
        await conn.run_sync(Base.metadata.create_all)

    #
    # async with engine.begin() as conn:
    #     inspector = inspect(engine)
    #
    #     if len(inspector.get_table_names())>3:
    #         await conn.run_sync(Base.metadata.create_all)
