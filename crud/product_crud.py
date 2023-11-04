from typing import overload

from fastapi import Depends
from sqlalchemy.orm import Session

from crud.crud import Crud
from db import get_session, ProductModel, ProductOrm
from sqlalchemy import select


class ProductCrud(Crud):
    def __init__(self, session: Session = Depends(get_session)):
        super().__init__(session)


    async def get_all(self) -> list[ProductModel]:
        result = self.session.execute(select(ProductOrm).order_by(ProductOrm.id).limit(20))
        return result.scalars().all()

    async def add_product(self, model) -> ProductModel:
        pass
        # new_product = ProductOrm(name=name)
        # session.add(new_product)
        # return new_product