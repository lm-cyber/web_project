from io import BytesIO
from typing import Sequence
import base64

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from shema import NewsImageOrm
from models import NewsImageModel, NewNewsImageModel


async def get(session: AsyncSession, id) -> NewsImageOrm:
    result = (await session.execute(select(NewsImageOrm).where(NewsImageOrm.id == id))).scalar_one_or_none()
    return NewsImageOrm(id=result.id, news_id=result.news_id, image=result.image)


async def delete_news_image(session: AsyncSession, id):
    stmt = delete(NewsImageOrm).where(NewsImageOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, id: int, image: bytes):
    new_image = NewsImageOrm(news_id=id, image=image)
    session.add(new_image)
    await session.commit()
    return {"id": new_image.id, "news_id": new_image.news_id}


async def update(session: AsyncSession, id: int, image: bytes):
    news_image = await session.get(NewsImageOrm, id)
    if not news_image:
        return None
    news_image.image = image
    await session.commit()
    return {"id": news_image.id, "product_id": news_image.news_id}
