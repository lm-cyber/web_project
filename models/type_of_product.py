from .models import Base

from sqlalchemy import Column, Integer, String, Sequence
from pydantic import BaseModel, ConfigDict, constr, conint


class TypeOfProductOrm(Base):
    __tablename__ = 'type_of_product'
    id = Column(Integer, Sequence('type_of_product_id_seq'), primary_key=True)
    name = Column(String(63), unique=True)


class NewTypeOfProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=63)
class TypeOfProductModel(NewTypeOfProductModel):

    id: int
    name: str