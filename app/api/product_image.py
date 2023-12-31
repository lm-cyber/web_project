from fastapi import Depends, APIRouter, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session

from fastapi.responses import Response
from crud import product_image_crud
from db import get_async_session
from models import NewProductImageModel, ProductImageModel, ImageByProductId
from fastapi import File
from shema import User
from auth import current_superuser_user

product_image_router = APIRouter(tags=["product_image"])


@product_image_router.post("/image/")
async def add_image(
    product_id: int,
    file_bytes: bytes = File(),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser_user),
):
    return await product_image_crud.create(session, product_id, file_bytes)


@product_image_router.delete("/image/{id}")
async def delete_image(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await product_image_crud.delete_product_image(session, id)


@product_image_router.put("/image/")
async def update_image(
    id: int,
    file_bytes: bytes = File(),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser_user),
):
    return await product_image_crud.update_product_image(session, id, file_bytes)


@product_image_router.get("/image/{id}", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
async def get_image(id: int = None, session: AsyncSession = Depends(get_async_session)):
    image_bytes = (await product_image_crud.get(session, id)).image
    return Response(content=image_bytes, media_type="image/png")


@product_image_router.get("/image_id_by_product_id/{id}")
async def get_image_id_by_product_id(id: int, session: AsyncSession = Depends(get_async_session)):
    return await product_image_crud.get_image_id_by_product_id(session, id)
