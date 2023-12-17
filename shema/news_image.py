from sqlalchemy.orm import relationship

from .base import Base

from sqlalchemy import Column, Integer, LargeBinary, Sequence, ForeignKey


class NewsImageOrm(Base):
    __tablename__ = "news_image"

    id = Column(Integer, Sequence("news_image_id_seq"), primary_key=True)
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False)
    image = Column(LargeBinary)
