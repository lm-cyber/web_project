from typing import List, Optional

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, LargeBinary
from pydantic import BaseModel, ConfigDict, constr, conint
from sqlalchemy.orm import relationship

from .models import Base


class ImageOrm(Base):
    __tablename__ = 'image'

    id = Column(Integer, Sequence('image_id_seq'), primary_key=True)
    # product_id = Column(Integer, ForeignKey('product.id'),nullable=False)
    image = Column(LargeBinary, nullable=False)


class NewImageWithoutBinary(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    # proudct_id: int
class NewImage(NewImageWithoutBinary):
    image: bytes


class Image(NewImage):
    id: int