from io import BytesIO
from typing import Sequence

from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import ProductImageOrm
from models import NewImageModel, ImageModel,ImageProductId


async def get_all(session: Session) -> Sequence[ImageModel]:
    result = session.execute(select(ProductImageOrm).order_by(ProductImageOrm.product_id)).scalars().all()
    return parse_obj_as(Sequence[ImageModel], result)


async def get(session: Session, id) -> ImageModel:
    result = session.execute(select(ProductImageOrm).where(ProductImageOrm.id == id)).scalar_one_or_none()
    return parse_obj_as(ImageModel, result)


async def delete(session: Session, id):
    session.query(ProductImageOrm).filter(ProductImageOrm.id == id).delete()
    session.commit()


async def create(session: Session, model: ImageProductId, binary_image: bytes) -> ImageModel:
    pass


async def update(session: Session, model: ImageModel) -> ImageModel | None:
    image: ProductImageOrm = session.query(ProductImageOrm).filter(ProductImageOrm.id == model.id).first()
    if not image:
        return None
    image.product_id = model.product_id
    image.binary_image = model.binary_image
    session.commit()
    return parse_obj_as(ImageModel, image)
