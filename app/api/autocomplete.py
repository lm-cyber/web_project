from typing import Optional

from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session

from db import get_async_session
from models import ProductModel, NewProductModel, AddedProduct
from crud import product_crud
from shema import User
from auth import current_superuser_user
from fastapi import FastAPI, Request

from fast_autocomplete import AutoComplete
import string


autocomplete_router = APIRouter(tags=["product"])


@autocomplete_router.get("/autocomplete/{word}")
async def get_product(word: str, session: AsyncSession = Depends(get_async_session)):
    async def create_autocomplete(data):
        import re
        from collections import Counter, defaultdict

        autocomplete_titles = defaultdict(lambda: {"count": 0})
        for row in data:
            words = row[0] + " " + row[1]
            words = re.sub("[^а-яА-ЯЁё0-9a-zA-Z ]", " ", words)
            words = words.lower()
            words = words.strip().split()
            cnt = Counter(words)
            for key, value in cnt.items():
                autocomplete_titles[key]["count"] += value
        autocomplete = AutoComplete(
            words=autocomplete_titles, valid_chars_for_string="абвгдеёжзийклмнопрстуфхцчшщьЪыэюя"
        )
        return autocomplete

    data = (await session.execute(text("SELECT name, description FROM product"))).all()
    autocomplete = await create_autocomplete(data)  # TODO change to production
    return autocomplete.search(word=word, max_cost=3, size=10)
