from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession


from db import get_async_session
from models import RequestProduct, NewRequestProduct, RequestProductName
from crud import request_crud
from shema import User
from auth import current_superuser_user

request_for_product_router = APIRouter(tags=["request_for_product"])


@request_for_product_router.get("/request_for_product/{id}", response_model=RequestProduct)
async def get_request(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await request_crud.get(session, id)


@request_for_product_router.get("/request_for_product_with_name/{id}", response_model=RequestProductName)
async def get_request_with_name(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await request_crud.get_with_name(session, id)


@request_for_product_router.get("/request_for_product/", response_model=list[RequestProduct])
async def get_request_all(
    session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await request_crud.get_all(session)


@request_for_product_router.get("/request_for_product_with_name/", response_model=list[RequestProductName] | None)
async def get_request_all_with_name(
    session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await request_crud.get_all_with_name(session)


@request_for_product_router.post("/request_for_product/", response_model=RequestProduct)
async def add_request(product: NewRequestProduct, session: AsyncSession = Depends(get_async_session)):
    return await request_crud.create(session, product)


@request_for_product_router.delete("/request_for_product/{id}")
async def delete_request(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    await request_crud.delete_request(session, id)
