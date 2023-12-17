from fastapi import Depends, APIRouter, UploadFile

from sqlalchemy.orm import Session

from fastapi.responses import Response
from crud import news_image_crud
from db import get_async_session
from fastapi import File

news_image_router = APIRouter(tags=["news_image"])


@news_image_router.post("/news_image/")
async def add_image(news_id: int, file_bytes: bytes = File(), session: Session = Depends(get_async_session)):
    return await news_image_crud.create(session, news_id, file_bytes)


@news_image_router.delete("/news_image/{id}")
async def delete_image(id: int, session: Session = Depends(get_async_session)):
    return await news_image_crud.delete(session, id)


@news_image_router.put("/news_image/")
async def update_image(id: int, file_bytes: bytes = File(), session: Session = Depends(get_async_session)):
    return await news_image_crud.update(session, id, file_bytes)


@news_image_router.get("/news_image/{id}", responses={200: {"content": {"image/png": {}}}}, response_class=Response)
async def get_image(id: int = None, session: Session = Depends(get_async_session)):
    image_bytes = (await news_image_crud.get(session, id)).image
    return Response(content=image_bytes, media_type="image/png")


@news_image_router.get("/image_id_by_news_id/{id}")
async def get_image_id_by_news_id(id: int, session: Session = Depends(get_async_session)):
    return await news_image_crud.get_image_id_by_news_id(session, id)
