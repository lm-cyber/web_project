from pydantic import BaseModel, ConfigDict


class NewCertImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    id: int


class CertImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    image: bytes
    id: int


class ImageByNewsId(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
