from typing import List, Optional

from pydantic import BaseModel, ConfigDict, constr, conint


class NewImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    image: bytes


class ImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    image: bytes
    id: int


class ImageProductId(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
