from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, ConfigDict, constr

Base = declarative_base()


class ProductOrm(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), unique=True)


class ProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=63)

