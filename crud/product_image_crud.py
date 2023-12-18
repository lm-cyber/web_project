from io import BytesIO
from typing import Sequence
import base64

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from sqlalchemy import select, delete
from shema import ProductImageOrm
from models import NewProductImageModel, ProductImageModel, ImageByProductId


async def get(session: AsyncSession, id) -> ProductImageModel:
    result = (await session.execute(select(ProductImageOrm).where(ProductImageOrm.id == id))).scalar_one_or_none()
    return ProductImageModel(id=result.id, product_id=result.product_id, image=result.image)


async def get_image_id_by_product_id(session: AsyncSession, id):
    result = (await session.execute(select(ProductImageOrm.id).filter(ProductImageOrm.product_id == id))).scalars().all()
    return result


async def delete_product_image(session: AsyncSession, id):
    stmt = (delete(ProductImageOrm).where(ProductImageOrm.id == id))
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, id: int, image: bytes):
    new_image = ProductImageOrm(product_id=id, image=image)
    session.add(new_image)
    await session.commit()
    return {"id": new_image.id, "product_id": new_image.product_id}

async def update_product_image(session: AsyncSession, id: int, image: bytes) -> ProductImageModel | None:
    image_product = await session.get(ProductImageOrm, id)
    image_product.image = image
    await session.commit()
    return {"id": image_product.id, "product_id": image_product.product_id}
