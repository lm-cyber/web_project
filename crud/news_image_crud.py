from io import BytesIO
from typing import Sequence
import base64
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from sqlalchemy import select
from shema import NewsImageOrm
from models import NewsImageModel, NewNewsImageModel, ImageByNewsId


async def get(session: Session, id) -> NewsImageModel:
    result = session.execute(select(NewsImageOrm).where(NewsImageOrm.id == id)).scalar_one_or_none()
    return NewsImageOrm(id=result.id, news_id=result.news_id, image=result.image)


async def get_image_id_by_news_id(session: Session, id):
    result = session.query(NewsImageOrm.id).filter(NewsImageOrm.news_id == id).all()
    return list(map(lambda x: x[0], result))


async def delete(session: Session, id):
    session.query(NewsImageOrm).filter(NewsImageOrm.id == id).delete()
    session.commit()


async def create(session: Session, id: int, image: bytes):
    new_image = NewsImageOrm(news_id=id, image=image)
    session.add(new_image)
    session.commit()
    return {"id": new_image.id, "news_id": new_image.news_id}


async def update(session: Session, id: int, image: bytes):
    image_product: NewsImageOrm = session.query(NewsImageOrm).filter(NewsImageOrm.id == id).first()
    if not image_product:
        return None

    image_product.image = image
    session.commit()
    return {"id": image_product.id, "news_id": image_product.news_id}