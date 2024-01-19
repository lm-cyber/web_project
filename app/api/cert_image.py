from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from shema import User
from auth import current_superuser_user

from fastapi.responses import Response
from crud import cert_image_crud
from db import get_async_session
from fastapi import File

cert_image_router = APIRouter(tags=["cert_image"])


@cert_image_router.post("/cert_image/")
async def add_image(
    cert_id: int,
    file_bytes: bytes = File(),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser_user),
):
    return await cert_image_crud.create(session, cert_id, file_bytes)


@cert_image_router.delete("/cert_image/{id}")
async def delete_image(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await cert_image_crud.delete_cert_image(session, id)


@cert_image_router.put("/cert_image/")
async def update_image(
    id: int,
    file_bytes: bytes = File(),
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser_user),
):
    return await cert_image_crud.update(session, id, file_bytes)


@cert_image_router.get("/cert_image/{id}", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
async def get_image(id: int = None, session: AsyncSession = Depends(get_async_session)):
    image_bytes = (await cert_image_crud.get(session, id)).image
    return Response(content=image_bytes, media_type="image/png")
