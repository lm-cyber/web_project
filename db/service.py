from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import ProductModel, ProductOrm


async def get_all_product(session: Session) -> list[ProductModel]:
    result = session.execute(select(ProductOrm).order_by(ProductOrm.id).limit(20))
    return result.scalars().all()


async def add_product(session: Session, name: str):
    new_product = ProductOrm(name=name)
    session.add(new_product)
    return new_product