from .base import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime


class RequestOrm(Base):
    __tablename__ = "request"

    id = Column(Integer, Sequence("request_id_seq"), primary_key=True)
    fio = Column(String(200))
    phone = Column(String(30))
    company = Column(String(128))
    email = Column(String(128))
    description_by_customer = Column(Text)
    datetime = Column(DateTime, default=datetime.now)
    request_product = relationship("RequestProductOrm", back_populates="request", lazy="selectin")
