from io import BytesIO
from typing import Sequence
import base64

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from shema import CertImageOrm
from models import CertImageModel, NewCertImageModel


async def get(session: AsyncSession, id) -> CertImageOrm:
    result = (await session.execute(select(CertImageOrm).where(CertImageOrm.id == id))).scalar_one_or_none()
    return CertImageOrm(id=result.id, cert_id=result.cert_id, image=result.image)


async def delete_cert_image(session: AsyncSession, id):
    stmt = delete(CertImageOrm).where(CertImageOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, id: int, image: bytes):
    new_image = CertImageOrm(cert_id=id, image=image)
    session.add(new_image)
    await session.commit()
    return {"id": new_image.id, "cert_id": new_image.cert_id}


async def update(session: AsyncSession, id: int, image: bytes):
    cert_image = await session.get(CertImageOrm, id)
    if not cert_image:
        return None
    cert_image.image = image
    await session.commit()
    return {"id": cert_image.id, "product_id": cert_image.cert_id}
