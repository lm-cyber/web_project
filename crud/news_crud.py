from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from sqlalchemy import select
from shema import NewsOrm
from models import NewsModel, NewNewsModel
from sqlalchemy import delete

async def get_all(session: AsyncSession) -> Sequence[NewsModel]:
    result = (await session.execute(select(NewsOrm).order_by(NewsOrm.name))).scalars().all()
    return parse_obj_as(Sequence[NewsModel], result)


async def get(session: AsyncSession, id) -> NewsModel:
    product = (await session.execute(select(NewsOrm).where(NewsOrm.id == id))).scalar_one_or_none()
    return parse_obj_as(NewsModel, product)


async def delete_news(session: AsyncSession, id):
    stmt = (delete(NewsOrm).where(NewsOrm.id == id))
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, model: NewNewsModel) -> NewsModel:
    new_product = NewsOrm(name=model.name, description=model.description)
    session.add(new_product)
    await session.commit()
    return parse_obj_as(NewsModel, new_product)


async def update(session: AsyncSession, model: NewNewsModel) -> NewsModel | None:
    news = await session.get(NewsOrm, model.id)
    if not news:
        return None
    news.name = model.name
    news.description = model.description
    await session.commit()
    return parse_obj_as(NewsModel, news)
