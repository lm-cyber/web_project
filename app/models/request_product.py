from pydantic import BaseModel, ConfigDict, constr, conint, EmailStr
from datetime import datetime


class ProductForRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    count: int


class NewRequestProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    fio: constr(max_length=300)
    phone: constr(max_length=30)
    company: constr(max_length=128)
    email: EmailStr
    description_by_customer: constr(max_length=1024)
    request_product: list[ProductForRequest]


class RequestProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fio: constr(max_length=300)
    phone: constr(max_length=30)
    company: constr(max_length=128)
    email: EmailStr
    description_by_customer: constr(max_length=1024)
    datetime: datetime
    request_product: list[ProductForRequest]


class ProductName(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: constr(max_length=128)


class ProductForRequestName(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product: ProductName
    count: int


class RequestProductName(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fio: constr(max_length=300)
    phone: constr(max_length=30)
    company: constr(max_length=128)
    email: EmailStr
    description_by_customer: constr(max_length=1024)
    datetime: datetime
    request_product: list[ProductForRequestName]
