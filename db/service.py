from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import (
    ProductModel,
    ProductOrm,
    TypeOfProductModel,
    TypeOfProductOrm,
    NewTypeOfProductModel,
    NewProductModel,
    NewImage,
    NewImageWithoutBinary,
    Image,
    ImageOrm
)


async def get_all_type_of_product(session: Session) -> Sequence[TypeOfProductOrm]:
    result = session.execute(select(TypeOfProductOrm).order_by(TypeOfProductOrm.id))
    return result.scalars().all()


async def get_type_of_product(session: Session, id: int) -> TypeOfProductModel:
    return session.execute(select(TypeOfProductOrm).where(TypeOfProductOrm.id == id)).scalar_one_or_none()


async def add_type_of_product(session: Session, type_of_product: NewTypeOfProductModel):
    new_type_of_product = TypeOfProductOrm(name=type_of_product.name)
    session.add(new_type_of_product)
    return new_type_of_product


async def update_type_of_product(session: Session, type_of_product_model: TypeOfProductModel):
    type_of_product = session.query(TypeOfProductOrm).filter(TypeOfProductOrm.id == type_of_product_model.id).first()
    if not type_of_product:
        return
    type_of_product.name = type_of_product_model.name
    session.commit()
    return type_of_product


async def delete_type_of_product(session: Session, id: int):
    session.query(TypeOfProductOrm).filter(TypeOfProductOrm.id == id).delete()
    session.commit()


async def add_image(session: Session, id, file_bytes):
    session.add(ImageOrm(image=file_bytes))
    session.commit()

async def get_image(session: Session, id:int=None):
    if id:
        return session.query(ImageOrm).filter(ImageOrm.id == id).first().scalar_one_or_none()
    return session.execute(select(ImageOrm).order_by(ImageOrm.id)).scalars().all()
