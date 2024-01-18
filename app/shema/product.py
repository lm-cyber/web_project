from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text, Computed, desc, Index, func
from sqlalchemy.orm import relationship, Mapped
from .base import Base

from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy import func, Index, cast, Text


class ProductOrm(Base):
    __tablename__ = "product"

    id = Column(Integer, Sequence("product_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    type_of_product_id = Column(Integer, ForeignKey("type_of_product.id"), nullable=False)
    __table_args__ = (
        Index('idx_product_name_trgm', 'name', postgresql_ops={'name': 'gin_trgm_ops'},
              postgresql_using='gin'),
        Index('idx_product_description_trgm', 'description', postgresql_ops={'description': 'gin_trgm_ops'},
              postgresql_using='gin'),
    )

    images = relationship("ProductImageOrm", backref="product", cascade="all,delete-orphan", lazy="selectin")
    request_product = relationship("RequestProductOrm", back_populates="product")
