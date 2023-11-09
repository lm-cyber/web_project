
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import type_of_product_crud
from db import get_session
from models import TypeOfProductModel, NewTypeOfProductModel

type_of_product_router = APIRouter()


@type_of_product_router.get("/type_of_product/", response_model=list[TypeOfProductModel] | TypeOfProductModel)
async def get_type_of_products(id: int = None,session: Session = Depends(get_session)):
    if id:
        return await type_of_product_crud.get(session,id)
    return await type_of_product_crud.get_all(session)


@type_of_product_router.post("/type_of_product/", response_model=TypeOfProductModel)
async def add_type_of_product(type_of_product: NewTypeOfProductModel, session: Session =Depends(get_session)):
    return await type_of_product_crud.create(session,type_of_product)


@type_of_product_router.delete("/type_of_product/")
async def delete_type_of_product(id: int, session: Session = Depends(get_session)):
    await type_of_product_crud.delete(session,id)


@type_of_product_router.put("/type_of_product/", response_model=TypeOfProductModel)
async def update_type_of_product(type_of_product: TypeOfProductModel, session: Session = Depends(get_session)):
    return await type_of_product_crud.update(session,type_of_product)
