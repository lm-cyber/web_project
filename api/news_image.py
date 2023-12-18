from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from shema import User
from auth import current_active_user

from fastapi.responses import Response
from crud import news_image_crud
from db import get_async_session
from fastapi import File

news_image_router = APIRouter(tags=["news_image"])


@news_image_router.post("/news_image/")
async def add_image(news_id: int, file_bytes: bytes = File(), session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await news_image_crud.create(session, news_id, file_bytes)


@news_image_router.delete("/news_image/{id}")
async def delete_image(id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await news_image_crud.delete_news_image(session, id)


@news_image_router.put("/news_image/")
async def update_image(id: int, file_bytes: bytes = File(), session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await news_image_crud.update(session, id, file_bytes)


@news_image_router.get("/news_image/{id}", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
async def get_image(id: int = None, session: AsyncSession = Depends(get_async_session)):
    image_bytes = (await news_image_crud.get(session, id)).image
    return Response(content=image_bytes, media_type="image/png")

