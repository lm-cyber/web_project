from typing import Sequence

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from shema import TypeOfProductOrm
from models import TypeOfProductModel, NewTypeOfProductModel
from sqlalchemy import select, delete


async def get_all(session: AsyncSession) -> Sequence[TypeOfProductModel]:
    result = (await session.execute(select(TypeOfProductOrm).order_by(TypeOfProductOrm.id))).scalars().all()
    return parse_obj_as(Sequence[TypeOfProductModel], result)


async def get(session: AsyncSession, id) -> TypeOfProductModel | None:
    result = (await session.execute(select(TypeOfProductOrm).where(TypeOfProductOrm.id == id))).scalar_one_or_none()
    if result:
        return parse_obj_as(TypeOfProductModel, result)
    return None


async def delete_type_of_product(session: AsyncSession, id):
    stmt = delete(TypeOfProductOrm).where(TypeOfProductOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, model: NewTypeOfProductModel) -> TypeOfProductModel:
    new_type_of_product = TypeOfProductOrm(name=model.name)
    session.add(new_type_of_product)
    await session.commit()
    return parse_obj_as(TypeOfProductModel, new_type_of_product)


async def update_type_of_product(session: AsyncSession, model: TypeOfProductModel):
    type_of_product = await session.get(TypeOfProductOrm, model.id)
    type_of_product.name = model.name
    await session.commit()
    return type_of_product
