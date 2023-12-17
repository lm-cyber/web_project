from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from sqlalchemy import select
from shema import NewsOrm
from models import NewsModel, NewNewsModel


async def get_all(session: Session) -> Sequence[NewsModel]:
    result = session.execute(select(NewsOrm).order_by(NewsOrm.name)).scalars().all()
    return parse_obj_as(Sequence[NewsModel], result)


async def get(session: Session, id) -> NewsModel:
    product = session.execute(select(NewsOrm).where(NewsOrm.id == id)).scalar_one_or_none()
    return parse_obj_as(NewsModel, product)


async def delete(session: Session, id):
    session.query(NewsOrm).filter(NewsOrm.id == id).delete()
    session.commit()


async def create(session: Session, model: NewNewsModel) -> NewsModel:
    new_product = NewsOrm(name=model.name, description=model.description)
    session.add(new_product)
    session.commit()
    return parse_obj_as(NewsModel, new_product)


async def update(session: Session, model: NewsModel) -> NewsModel | None:
    product: NewsOrm = session.query(NewsOrm).filter(NewsOrm.id == model.id).first()
    if not product:
        return None
    product.name = model.name
    product.type_of_product_id = model.type_of_product_id
    product.description = model.description
    session.commit()
    return parse_obj_as(NewsModel, product)
