from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, joinedload
from collections import defaultdict
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import NewsOrm, NewsImageOrm
from models import NewsModel, NewNewsModel, NewsImageModel, NewsAdded
from sqlalchemy import delete


async def get_all(session: AsyncSession) -> Sequence[NewsModel]:
    result = await session.execute(select(NewsOrm).options(joinedload(NewsOrm.images).load_only(NewsImageOrm.id)))
    result = result.unique().scalars().all()
    return parse_obj_as(Sequence[NewsModel], result)


async def get(session: AsyncSession, id) -> NewsModel:
    result = await session.execute(
        select(NewsOrm).options(joinedload(NewsOrm.images).load_only(NewsImageOrm.id)).filter(NewsOrm.id == id)
    )
    result = result.unique().scalar_one_or_none()
    return parse_obj_as(NewsModel, result)


async def delete_news(session: AsyncSession, id):
    stmt = delete(NewsOrm).where(NewsOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, model: NewNewsModel) -> NewsAdded:
    news = NewsOrm(name=model.name, description=model.description)
    session.add(news)
    await session.commit()
    return parse_obj_as(NewsAdded, news)


async def update(session: AsyncSession, model: NewNewsModel) -> NewsAdded | None:
    news = await session.get(NewsOrm, model.id)
    if not news:
        return None
    news.name = model.name
    news.description = model.description
    await session.commit()
    return parse_obj_as(NewsAdded, news)
