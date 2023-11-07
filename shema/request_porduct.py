from .base import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text
from sqlalchemy.orm import relationship


class RequestProductOrm(Base):
    __tablename__ = 'request_product'

    id = Column(Integer, Sequence('request_id_seq'), primary_key=True)
    name = Column(String(64))
    surname = Column(String(64))
    patronymic = Column(String(64))
    company = Column(String(128))
    email = Column(String(128))
    under_request = Column(Text(1024))
    product_in_request = relationship("ProductInRequestOrm", back_populates="request_product")