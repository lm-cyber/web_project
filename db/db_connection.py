from typing import Generator

from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shema.base import Base

engine: Engine = create_engine("postgresql+psycopg2://docker:docker@localhost/docker")

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