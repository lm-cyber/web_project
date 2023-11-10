from typing import List, Optional

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text
from sqlalchemy.orm import relationship

from .base import Base


class ProductOrm(Base):
    __tablename__ = "product"

    id = Column(Integer, Sequence("product_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)

    type_of_product_id = Column(Integer, ForeignKey("type_of_product.id"), nullable=False)
    images = relationship("ProductImageOrm", backref="product_relation_to")
