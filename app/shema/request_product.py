from .base import Base
from sqlalchemy import Column, Integer, ForeignKey, Sequence
from sqlalchemy.orm import relationship, mapped_column


class RequestProductOrm(Base):
    __tablename__ = "request_product"


    # request_id = mapped_column(ForeignKey("request.id"), nullable=False,primary_key=True)
    # product_id = mapped_column(ForeignKey("product.id"), nullable=False,primary_key=True)
    count = Column(Integer, nullable=False, default=1, primary_key=True)
