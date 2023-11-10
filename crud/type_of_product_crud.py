from typing import Sequence

from fastapi import Depends
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from sqlalchemy import select
from shema import TypeOfProductOrm
from models import TypeOfProductModel, NewTypeOfProductModel


async def get_all(session: Session) -> Sequence[TypeOfProductModel]:
    result = session.execute(select(TypeOfProductOrm).order_by(TypeOfProductOrm.id)).scalars().all()
    return parse_obj_as(Sequence[TypeOfProductModel], result)


async def get(session: Session, id) -> TypeOfProductModel | None:
    result = session.execute(select(TypeOfProductOrm).where(TypeOfProductOrm.id == id)).scalar_one_or_none()
    if result:
        return parse_obj_as(TypeOfProductModel, result)
    return None


async def delete(session: Session, id):
    session.query(TypeOfProductOrm).filter(TypeOfProductOrm.id == id).delete()
    session.commit()


async def create(session: Session, model: NewTypeOfProductModel) -> TypeOfProductModel:
    new_type_of_product = TypeOfProductOrm(name=model.name)
    session.add(new_type_of_product)
    session.commit()
    return parse_obj_as(TypeOfProductModel, new_type_of_product)


async def update(session: Session, model: TypeOfProductModel) -> TypeOfProductModel:
    type_of_product = session.query(TypeOfProductOrm).filter(TypeOfProductOrm.id == model.id).first()
    if not type_of_product:
        return
    type_of_product.name = model.name
    session.commit()
    return parse_obj_as(TypeOfProductModel, type_of_product)
