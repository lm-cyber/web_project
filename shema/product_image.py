from sqlalchemy.orm import relationship

from .base import Base

from sqlalchemy import Column, Integer, LargeBinary, Sequence, ForeignKey


class ProductImageOrm(Base):
    __tablename__ = 'product_image'

    id = Column(Integer, Sequence('product_image_id_seq'), primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    product = relationship("ProductOrm", back_populates="product_image")
    binary_image = Column(LargeBinary)