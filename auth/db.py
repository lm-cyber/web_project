from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from ..db.db_connection import get_session
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from ..shema.base import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


import uuid

from fastapi_users import FastAPIUsers

from .transport import auth_backend
from .user_manager import get_user_manager

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],

)
async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)