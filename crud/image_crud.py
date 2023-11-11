from io import BytesIO
from typing import Sequence
import base64
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import ProductImageOrm
from models import NewImageModel, ImageModel, ImageProductId


async def get_all(session: Session):  # -> Sequence[ImageModel]:
    result = session.execute(select(ProductImageOrm).order_by(ProductImageOrm.product_id)).scalars().all()
    # return parse_obj_as(Sequence[ImageModel], result)
    return result


async def get(session: Session, id) -> ImageModel:
    result = session.execute(select(ProductImageOrm).where(ProductImageOrm.id == id)).scalar_one_or_none()
    return ImageModel(id=result.id, product_id=result.product_id, image=result.image)


async def delete(session: Session, id):
    session.query(ProductImageOrm).filter(ProductImageOrm.id == id).delete()
    session.commit()


async def create(session: Session, id: int, image: bytes):
    new_image = ProductImageOrm(product_id=id, image=image)
    session.add(new_image)
    session.commit()
    return {"id": new_image.id, "product_id": new_image.product_id}
    # return ImageModel(id=new_image.id,product_id=new_image.product_id, binary_image=new_image.binary_image)


async def update(session: Session, model: ImageModel) -> ImageModel | None:
    image: ProductImageOrm = session.query(ProductImageOrm).filter(ProductImageOrm.id == model.id).first()
    if not image:
        return None
    image.product_id = model.product_id
    image.binary_image = model.binary_image
    session.commit()
    return parse_obj_as(ImageModel, image)
