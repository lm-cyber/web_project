from io import BytesIO
from typing import Sequence
import base64

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from shema import CertImageOrm
from models import CertImageModel, NewCertImageModel


async def get(session: AsyncSession, id) -> CertImageOrm:
    result = (await session.execute(select(CertImageOrm).where(CertImageOrm.id == id))).scalar_one_or_none()
    return CertImageOrm(id=result.id, news_id=result.cert_id, image=result.image)


async def delete_cert_image(session: AsyncSession, id):
    stmt = delete(CertImageOrm).where(CertImageOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, id: int, image: bytes):
    new_image = CertImageOrm(news_id=id, image=image)
    session.add(new_image)
    await session.commit()
    return {"id": new_image.id, "news_id": new_image.cert_id}


async def update(session: AsyncSession, id: int, image: bytes):
    news_image = await session.get(CertImageOrm, id)
    if not news_image:
        return None
    news_image.image = image
    await session.commit()
    return {"id": news_image.id, "product_id": news_image.cert_id}
