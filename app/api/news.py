from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session
from shema import User
from auth import current_superuser_user

from db import get_async_session
from models import NewsModel, NewNewsModel, NewsAdded
from crud import news_crud

news_router = APIRouter()


@news_router.get("/news/{id}", response_model=NewsModel)
async def get_news(id: int, session: AsyncSession = Depends(get_async_session)):
    return await news_crud.get(session, id)


@news_router.get("/news/", response_model=list[NewsModel])
async def get_newses(session: AsyncSession = Depends(get_async_session)):
    return await news_crud.get_all(session)


@news_router.post("/news/", response_model=NewsAdded)
async def add_news(
    news: NewNewsModel, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await news_crud.create(session, news)


@news_router.delete("/news/{id}")
async def delete_news(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    await news_crud.delete_news(session, id)


@news_router.put("/news/", response_model=NewsAdded)
async def update_news(
    news: NewsAdded, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await news_crud.update(session, news)
