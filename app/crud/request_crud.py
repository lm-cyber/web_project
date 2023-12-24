from typing import Sequence, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import RequestProductOrm, RequestOrm, ProductOrm
from models import RequestProduct, NewRequestProduct, RequestProductName
from sqlalchemy import delete


async def get_all_with_name(session: AsyncSession) -> Sequence[RequestProductName]:
    result = await session.execute(
        select(RequestOrm).options(
            joinedload(RequestOrm.request_product)
            .load_only(RequestProductOrm.count)
            .joinedload(RequestProductOrm.product)
            .load_only(ProductOrm.name)
        )
    )

    result = result.unique().scalars().all()
    return parse_obj_as(Sequence[RequestProductName], result)


async def get_with_name(session: AsyncSession, id) -> Sequence[RequestProductName]:
    result = await session.execute(
        select(RequestOrm)
        .options(
            joinedload(RequestOrm.request_product)
            .load_only(RequestProductOrm.count)
            .joinedload(RequestProductOrm.product)
            .load_only(ProductOrm.name)
        )
        .where(RequestOrm.id == id)
    )

    result = result.unique().scalar_one_or_none()
    return parse_obj_as(RequestProductName, result)


async def get_all(session: AsyncSession) -> Sequence[RequestProduct]:
    result = await session.execute(
        select(RequestOrm).options(
            joinedload(RequestOrm.request_product).load_only(RequestProductOrm.product_id, RequestProductOrm.count)
        )
    )

    result = result.unique().scalars().all()
    return parse_obj_as(Sequence[RequestProduct], result)


async def get(session: AsyncSession, id) -> RequestProduct:
    result = await session.execute(
        select(RequestOrm)
        .options(joinedload(RequestOrm.request_product).load_only(RequestProductOrm.product_id, RequestProductOrm.count))
        .where(RequestOrm.id == id)
    )
    result = result.unique().scalar_one_or_none()
    return parse_obj_as(RequestProduct, result)


async def delete_request(session: AsyncSession, id):
    stmt = delete(RequestOrm).where(RequestOrm.id == id)
    await session.execute(stmt)
    await session.commit()


async def create(session: AsyncSession, model: NewRequestProduct) -> RequestProduct:
    product_for_request = model.request_product
    product_for_request_orm = [
        RequestProductOrm(product_id=product.product_id, count=product.count) for product in product_for_request
    ]
    request_product = RequestOrm(
        fio=model.fio,
        phone=model.phone,
        company=model.company,
        email=model.email,
        description_by_customer=model.description_by_customer,
        request_product=product_for_request_orm,
    )
    session.add(request_product)
    await session.commit()
    return parse_obj_as(RequestProduct, request_product)
