from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import ProductModel, ProductOrm, TypeOfProductModel, TypeOfProductOrm, NewTypeOfProductModel, NewProductModel


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
async def get_all_product(session: Session) -> Sequence[ProductOrm]:
    result = session.execute(select(ProductOrm).order_by(ProductOrm.id).limit(20))
    return result.scalars().all()


async def add_product(session: Session, product: NewProductModel) -> ProductModel:
    new_product = ProductOrm(name=product.name, type_of_product=product.type_of_product)
    session.add(new_product)
    return new_product


async def delete_product(session: Session, id: int):
    session.query(ProductOrm).filter(ProductOrm.id == id).delete()
    session.commit()


async def update_product(session: Session, product_model: ProductModel):
    product = session.query(ProductOrm).filter(ProductOrm.id == product_model.id).first()
    if not product:
        return
    product.name = product_model.name
    product.type_of_product = product_model.type_of_product
    session.commit()
    return product


async def get_product(session: Session, id: int) -> ProductModel:
    return session.execute(select(ProductOrm).where(ProductOrm.id == id)).scalar_one_or_none()
