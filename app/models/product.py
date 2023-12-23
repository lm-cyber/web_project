from pydantic import BaseModel, ConfigDict, constr, conint

class NewProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=128)
    type_of_product_id: int
    description: constr(max_length=1024)


class Image(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int

class CreatedProduct(NewProductModel):
    id: int
class ProductModel(CreatedProduct):
    images: list[Image]

