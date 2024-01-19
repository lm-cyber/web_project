from sqlalchemy.orm import relationship

from .base import Base

from sqlalchemy import Column, Integer, LargeBinary, Sequence, ForeignKey


class CertImageOrm(Base):
    __tablename__ = "cert_image"

    id = Column(Integer, Sequence("cert_image_id_seq"), primary_key=True)
    cert_id = Column(Integer, ForeignKey("cert.id", ondelete="CASCADE"), nullable=False)
    image = Column(LargeBinary)
