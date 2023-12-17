from typing import Optional

from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import get_session
from models import ProductModel, NewProductModel
from crud import product_crud

product_router = APIRouter(tags=["product"])


@product_router.get("/product/{id}", response_model=ProductModel)
async def get_product(id: int, session: Session = Depends(get_session)):
    return await product_crud.get(session, id)

@product_router.get("/product/", response_model=list[ProductModel])
async def get_products(session: Session = Depends(get_session)):
    return await product_crud.get_all(session)


@product_router.post("/product/", response_model=ProductModel)
async def add_product(product: NewProductModel, session: Session = Depends(get_session)):
    return await product_crud.create(session, product)


@product_router.delete("/product/{id}")
async def delete_product(id: int, session: Session = Depends(get_session)):
    await product_crud.delete(session, id)


@product_router.put("/product/", response_model=ProductModel)
async def update_product(product: ProductModel, session: Session = Depends(get_session)):
    return await product_crud.update(session, product)
