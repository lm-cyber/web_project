from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import get_session
from models import NewsModel, NewNewsModel
from crud import news_crud

news_router = APIRouter()


@news_router.get("/news/{id}", response_model=list[NewsModel] | NewsModel)
async def get_products(id: int = None, session: Session = Depends(get_session)):
    if id:
        return await news_crud.get(session, id)
    return await news_crud.get_all(session)


@news_router.post("/news/", response_model=NewsModel)
async def add_product(product: NewNewsModel, session: Session = Depends(get_session)):
    return await news_crud.create(session, product)


@news_router.delete("/news/{id}")
async def delete_product(id: int, session: Session = Depends(get_session)):
    await news_crud.delete(session, id)


@news_router.put("/news/", response_model=NewsModel)
async def update_product(product: NewsModel, session: Session = Depends(get_session)):
    return await news_crud.update(session, product)
