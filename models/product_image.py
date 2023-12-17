from pydantic import BaseModel, ConfigDict


class NewProductImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    id: int


class ProductImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    image: bytes
    id: int


class ImageByProductId(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
