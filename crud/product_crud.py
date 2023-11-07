from typing import overload, Sequence

from fastapi import Depends
from sqlalchemy.orm import Session

from .crud import Crud
from db import get_session
from sqlalchemy import select
from models import ProductOrm


class ProductCrud(Crud):
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(session)

    async def get_all(self) -> Sequence[ProductOrm]:
        result = self._session.execute(select(ProductOrm).order_by(ProductOrm.name))
        return result.scalars().all()

    async def get(self, id):
        return await super().get(id)

    async def delete(self, id):
        return await super().delete(id)

    async def create(self, model):
        return await super().create(model)

    async def update(self, model):
        return await super().update(model)

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

