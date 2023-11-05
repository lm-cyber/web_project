from typing import Generator

from sqlalchemy import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.models import Base

engine: Engine = create_engine("postgresql+psycopg2://docker:docker@localhost/docker")


def init_models():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


session = Session(bind=engine)



def get_session() -> Generator:
    try:
        yield session
    finally:
        session.close()