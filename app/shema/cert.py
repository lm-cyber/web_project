from sqlalchemy import Column, Integer, String, Sequence, Text
from sqlalchemy.orm import relationship

from .base import Base


class CertOrm(Base):
    __tablename__ = "cert"

    id = Column(Integer, Sequence("cert_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    images = relationship("CertImageOrm", backref="cert", cascade="all,delete-orphan", lazy="selectin")
