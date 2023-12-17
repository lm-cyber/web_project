from typing import Generator

from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shema.base import Base


from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER



DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
engine: Engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_models():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_session() -> Generator:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
