from sqlalchemy import Column, Integer, String, Sequence, Text
from sqlalchemy.orm import relationship

from .base import Base


class NewsOrm(Base):
    __tablename__ = "news"

    id = Column(Integer, Sequence("news_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    images = relationship("NewsImageOrm", backref="news", cascade="all,delete-orphan", lazy="selectin")
