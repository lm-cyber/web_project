from typing import Sequence, List

from fastapi import Depends
from sqlalchemy.orm import Session

from pydantic import parse_obj_as
from sqlalchemy import select
from shema import ProductOrm
from models import ProductModel, NewProductModel


async def get_all(session: Session) -> Sequence[ProductModel]:
    result = session.execute(select(ProductOrm).order_by(ProductOrm.name)).scalars().all()
    return parse_obj_as(Sequence[ProductModel], result)


async def get(session: Session, id) -> ProductModel:
    product = session.execute(select(ProductOrm).where(ProductOrm.id == id)).scalar_one_or_none()
    return parse_obj_as(ProductModel, product)


async def delete(session: Session, id):
    session.query(ProductOrm).filter(ProductOrm.id == id).delete()
    session.commit()


async def create(session: Session, model: NewProductModel) -> ProductModel:
    new_product = ProductOrm(name=model.name, type_of_product_id=model.type_of_product_id, description=model.description)
    session.add(new_product)
    session.commit()
    return parse_obj_as(ProductModel, new_product)


async def update(session: Session, model: ProductModel) -> ProductModel | None:
    product: ProductOrm = session.query(ProductOrm).filter(ProductOrm.id == model.id).first()
    if not product:
        return None
    product.name = model.name
    product.type_of_product_id = model.type_of_product_id
    product.description = model.description
    session.commit()
    return parse_obj_as(ProductModel, product)
