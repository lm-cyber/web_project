from typing import Optional

from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session

from db import get_async_session
from models import ProductModel, NewProductModel, AddedProduct
from crud import product_crud
from shema import User
from auth import current_superuser_user

product_router = APIRouter(tags=["product"])


@product_router.get("/product/{id}", response_model=ProductModel)
async def get_product(id: int, session: AsyncSession = Depends(get_async_session)):
    return await product_crud.get(session, id)

@product_router.get("/product/", response_model=list[ProductModel])
async def get_products(session: AsyncSession = Depends(get_async_session)):
    return await product_crud.get_all(session)


@product_router.post("/product/", response_model=AddedProduct)
async def add_product(product: NewProductModel, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)):
    return await product_crud.create(session, product)


@product_router.delete("/product/{id}")
async def delete_product(id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)):
    await product_crud.delete_product(session, id)


@product_router.put("/product/", response_model=AddedProduct)
async def update_product(product: AddedProduct, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)):
    return await product_crud.update_product(session, product)
