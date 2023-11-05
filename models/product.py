from typing import List, Optional

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from pydantic import BaseModel, ConfigDict, constr, conint
from sqlalchemy.orm import relationship

from .models import Base


class ProductOrm(Base):
    __tablename__ = 'product'

    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    name = Column(String(63), unique=True)
    type_of_product = Column(Integer, ForeignKey("type_of_product.id"), nullable=False)


class NewProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=63)
    type_of_product: int
class ProductModel(NewProductModel):

    id: int

