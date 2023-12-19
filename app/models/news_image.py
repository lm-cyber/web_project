from pydantic import BaseModel, ConfigDict


class NewNewsImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    id: int


class NewsImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    image: bytes
    id: int


class ImageByNewsId(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
