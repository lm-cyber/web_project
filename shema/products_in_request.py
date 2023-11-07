from .base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class ProductInRequestOrm(Base):
    __tablename__ = 'product_in_request'

    request_id = Column(Integer, ForeignKey('request_product.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    count = Column(Integer, nullable=False, default=1)
    request_relation = relationship("RequestProductOrm", back_populates="product_in_request")
    product_relation = relationship("ProductOrm", back_populates="product_in_request")
