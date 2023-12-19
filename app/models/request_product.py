from pydantic import BaseModel, ConfigDict, constr, datetime_parse, conint, EmailStr


class NewRequestProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    fio: constr(max_length=300)
    phone: constr(max_length=30)
    company: constr(max_length=128)
    email: EmailStr
    under_request: constr(max_length=1024)
    product_ids: list[int]


class RequestProduct(NewRequestProduct):
    id: int
    datetime: datetime_parse
