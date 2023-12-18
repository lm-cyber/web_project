from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from crud import type_of_product_crud
from db import get_async_session
from models import TypeOfProductModel, NewTypeOfProductModel
from shema import User
from auth import current_active_user

type_of_product_router = APIRouter(tags=["type_of_product"])


@type_of_product_router.get("/type_of_product/{id}", response_model=TypeOfProductModel)
async def get_type_of_product(id: int = None, session: AsyncSession = Depends(get_async_session)):
    return await type_of_product_crud.get(session, id)


@type_of_product_router.get("/type_of_product/", response_model=list[TypeOfProductModel])
async def get_type_of_products(session: AsyncSession = Depends(get_async_session)):
    return await type_of_product_crud.get_all(session)
@type_of_product_router.post("/type_of_product/", response_model=TypeOfProductModel)
async def add_type_of_product(type_of_product: NewTypeOfProductModel, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await type_of_product_crud.create(session, type_of_product)


@type_of_product_router.delete("/type_of_product/{id}")
async def delete_type_of_product(id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    await type_of_product_crud.delete_type_of_product(session, id)


@type_of_product_router.put("/type_of_product/", response_model=TypeOfProductModel)
async def update_type_of_product(type_of_product: TypeOfProductModel, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await type_of_product_crud.update_type_of_product(session, type_of_product)
