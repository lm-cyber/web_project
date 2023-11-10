from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship


class ProductInRequestOrm(Base):
    __tablename__ = "product_in_request"

    id = Column(Integer, Sequence("product_in_request_id_seq"), primary_key=True)
    request_id = Column(Integer, ForeignKey("request_product.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    count = Column(Integer, nullable=False, default=1)
    product = relationship("ProductOrm", backref="product_in_request")
