from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import service
from db import get_session
from models import TypeOfProductModel, NewTypeOfProductModel, TypeOfProductOrm
type_of_product_router = APIRouter()

@type_of_product_router.get("/type_of_product/")
async def get_type_of_products(session: Session = Depends(get_session), id: int = None):
    if id:
        type_of_product = await service.get_type_of_product(session, id)
        return TypeOfProductModel(id=type_of_product.id, name=type_of_product.name)
    type_of_products = await service.get_all_type_of_product(session)
    return [TypeOfProductModel(id=c.id, name=c.name) for c in type_of_products]


@type_of_product_router.post("/type_of_product/")
async def add_type_of_product(type_of_poduct: NewTypeOfProductModel, session: Session = Depends(get_session)):
    type_of_poduct = await service.add_type_of_product(session, type_of_poduct)
    session.commit()
    return type_of_poduct


@type_of_product_router.delete("/type_of_product/")
async def delete_type_of_product(id: int, session: Session = Depends(get_session)):
    await service.delete_type_of_product(session, id)
    session.commit()

@type_of_product_router.put("/type_of_product/")
async def update_type_of_product(type_of_product: TypeOfProductModel, session: Session = Depends(get_session)):
    await service.update_type_of_product(session, type_of_product)
    session.commit()


