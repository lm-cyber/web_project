
from pydantic import BaseModel, ConfigDict, constr, conint





class NewTypeOfProductModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=128)
class TypeOfProductModel(NewTypeOfProductModel):

    id: int
