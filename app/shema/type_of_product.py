from sqlalchemy.orm import relationship

from .base import Base

from sqlalchemy import Column, Integer, String, Sequence


class TypeOfProductOrm(Base):
    __tablename__ = "type_of_product"

    id = Column(Integer, Sequence("type_of_product_id_seq"), primary_key=True)
    name = Column(String(63), unique=True)
    product = relationship("ProductOrm", backref="type_of_product")
