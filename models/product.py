
from pydantic import BaseModel, ConfigDict, constr, conint

class NewProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=63)
    type_of_product: int
class ProductModel(NewProductModel):

    id: int