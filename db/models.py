from typing import List, Optional

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, ConfigDict, constr, conint

Base = declarative_base()


class ProductOrm(Base):
    __tablename__ = 'product'

    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(63), unique=True)


class NewProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=63)
class ProductModel(NewProductModel):

    id: int

