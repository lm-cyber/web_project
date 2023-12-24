from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship, mapped_column, Mapped


class RequestProductOrm(Base):
    __tablename__ = "request_product"

    id = Column(Integer, Sequence("request_product_id_seq"), primary_key=True)
    request_id = Column(Integer, ForeignKey("request.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False, default=1, primary_key=True)
    request = relationship("RequestOrm", back_populates="request_product", lazy="selectin")
    product = relationship("ProductOrm", back_populates="request_product", lazy="selectin")
