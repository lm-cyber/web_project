from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import ProductModel, ProductOrm


async def get_all_product(session: Session) -> list[ProductModel]:
    result = session.execute(select(ProductOrm).order_by(ProductOrm.id).limit(20))
    return result.scalars().all()


async def add_product(session: Session,name: str) -> ProductModel:
    new_product = ProductOrm(name=name)
    session.add(new_product)
    return new_product


async def delete_product(session: Session, id: int):
    session.query(ProductOrm).filter(ProductOrm.id == id).delete()
    session.commit()


async def update_product(session: Session, id: int, name: str):
    product = session.query(ProductOrm).filter(ProductOrm.id == id).first()
    if not product:
        return
    product.name = name
    session.commit()
    return product

async def get_product(session: Session, id: int) -> ProductModel:
    return session.execute(select(ProductOrm).where(ProductOrm.id == id)).scalar_one_or_none()