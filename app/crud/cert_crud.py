from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, joinedload
from collections import defaultdict
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import CertOrm, CertImageOrm
from models import CertModel, NewCertModel, CertImageModel, CertAdded
from sqlalchemy import delete


async def get_all(session: AsyncSession) -> Sequence[CertModel]:
    result = await session.execute(select(CertOrm).options(joinedload(CertOrm.images).load_only(CertImageOrm.id)))
    result = result.unique().scalars().all()
    return parse_obj_as(Sequence[CertModel], result)


async def get(session: AsyncSession, id) -> CertModel:
    result = await session.execute(
        select(CertOrm).options(joinedload(CertOrm.images).load_only(CertImageOrm.id)).filter(CertOrm.id == id)
    )
    result = result.unique().scalar_one_or_none()
    return parse_obj_as(CertModel, result)


async def delete_news(session: AsyncSession, id):
    stmt = delete(CertOrm).where(CertOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, model: NewCertModel) -> CertAdded:
    news = CertOrm(name=model.name, description=model.description)
    session.add(news)
    await session.commit()
    return parse_obj_as(CertAdded, news)


async def update(session: AsyncSession, model: NewCertModel) -> CertAdded | None:
    news = await session.get(CertOrm, model.id)
    if not news:
        return None
    news.name = model.name
    news.description = model.description
    await session.commit()
    return parse_obj_as(CertAdded, news)
