from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import service
from db import get_session
from models import ProductModel, NewProductModel
from crud import product_crud

product_router = APIRouter()


@product_router.get("/product/", response_model=list[ProductModel] | ProductModel)
async def get_products(id: int = None, session: Session = Depends(get_session)):
    if id:
        return await product_crud.get(session, id)
    return await product_crud.get_all(session)


@product_router.post("/product/", response_model=ProductModel)
async def add_product(product: NewProductModel, session: Session = Depends(get_session)):
    return await product_crud.create(session, product)


@product_router.delete("/product/")
async def delete_product(id: int, session: Session = Depends(get_session)):
    await product_crud.delete(session, id)


@product_router.put("/product/", response_model=ProductModel)
async def update_product(product: ProductModel, session: Session = Depends(get_session)):
    return await product_crud.update(session, product)
