from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from sqlalchemy import select
from shema import ProductOrm
from models import ProductModel, NewProductModel


async def get_all(session: AsyncSession) -> Sequence[ProductModel]:
    result = (await session.execute(select(ProductOrm).order_by(ProductOrm.name))).scalars().all()
    return parse_obj_as(Sequence[ProductModel], result)


async def get(session: AsyncSession, id) -> ProductModel:
    product = (await session.execute(select(ProductOrm).where(ProductOrm.id == id))).scalar_one()
    return parse_obj_as(ProductModel, product)


async def delete(session: AsyncSession, id):
    await session.delete((await session.execute(select(ProductOrm).where(ProductOrm.id == id))).scalar_one())
    await session.commit()


async def create(session: AsyncSession, model: NewProductModel) -> ProductModel:
    new_product = ProductOrm(name=model.name, type_of_product_id=model.type_of_product_id, description=model.description)
    session.add(new_product)
    await session.commit()
    return parse_obj_as(ProductModel, new_product)


async def update(session: AsyncSession, model: ProductModel) -> ProductModel | None:
    product: ProductOrm = await session.query(ProductOrm).filter(ProductOrm.id == model.id).first()
    if not product:
        return None
    product.name = model.name
    product.type_of_product_id = model.type_of_product_id
    product.description = model.description
    await session.commit()
    return parse_obj_as(ProductModel, product)
