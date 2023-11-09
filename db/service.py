from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session




#
#
# async def add_image(session: Session, id, file_bytes):
#     session.add(ImageOrm(image=file_bytes))
#     session.commit()
#
# async def get_image(session: Session, id:int=None):
#     if id:
#         return session.query(ImageOrm).filter(ImageOrm.id == id).first().scalar_one_or_none()
#     return session.execute(select(ImageOrm).order_by(ImageOrm.id)).scalars().all()
