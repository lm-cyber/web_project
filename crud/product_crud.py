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
       pass # TODO


    async def add_product(self, model) -> ProductModel:
        pass # TODO