from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship, mapped_column


class RequestProductOrm(Base):
    __tablename__ = "request_product"

    id = Column(Integer, Sequence("request_product_id_seq"), primary_key=True)
    # product_id = mapped_column(ForeignKey("product.id"), nullable=False,primary_key=True)
    # count = Column(Integer, nullable=False, default=1, primary_key=True)
