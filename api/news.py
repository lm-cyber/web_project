from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import get_session
from models import NewsModel, NewNewsModel
from crud import news_crud

news_router = APIRouter()


@news_router.get("/news/{id}", response_model=NewsModel)
async def get_news(id: int, session: Session = Depends(get_session)):
    return await news_crud.get(session, id)
@news_router.get("/news/", response_model=list[NewsModel])
async def get_newses(session: Session = Depends(get_session)):
    return await news_crud.get_all(session)

@news_router.post("/news/", response_model=NewsModel)
async def add_news(news: NewNewsModel, session: Session = Depends(get_session)):
    return await news_crud.create(session, news)


@news_router.delete("/news/{id}")
async def delete_news(id: int, session: Session = Depends(get_session)):
    await news_crud.delete(session, id)


@news_router.put("/news/", response_model=NewsModel)
async def update_news(news: NewsModel, session: Session = Depends(get_session)):
    return await news_crud.update(session, news)
