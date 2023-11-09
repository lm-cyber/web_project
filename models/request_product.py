
from pydantic import BaseModel, ConfigDict, constr, datetime_parse,conint

class NewRequestProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name : constr(max_length=64)
    surname: constr(max_length=64)
    patronymic: constr(max_length=64)
    company: constr(max_length=128)
    email : constr(max_length=128)
    under_request: constr(max_length=1024)


class RequestProduct(NewRequestProduct):

    id: int
    datetime: datetime_parse

