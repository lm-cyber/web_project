from pydantic import BaseModel, ConfigDict, constr, conint

class NewProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=128)
    type_of_product_id: int
    description: constr(max_length=1024)


class ProductModel(NewProductModel):
    id: int
    images: list[int]
