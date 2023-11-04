from fastapi import Depends
from sqlalchemy.orm import Session

from db import get_session, ProductModel, ProductOrm
from sqlalchemy import select


class Crud:
    def __init__(self, session: Session = Depends(get_session)):
        self._session = session

    async def get_all(self) -> list:
        pass

    async def get(self, id):
        pass

    async def delete(self, id):
        pass
    async def create(self, model):
        pass

    async def update(self, model):
        pass

