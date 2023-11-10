from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session


from crud import image_crud
from db import get_session
from models import NewImageModel, ImageModel, ImageProductId
from fastapi import File

image_router = APIRouter()


@image_router.get("/image/")
async def get_image(session: Session = Depends(get_session), id: int = None):
    if id:
        return await image_crud.get(session, id)
    return await image_crud.get_all(session)


@image_router.post("/image/")
async def add_image(image: ImageProductId, file_bytes: bytes = File(), session: Session = Depends(get_session)):
    await image_crud.create(session, image, file_bytes)
    return {"status": "ok"}  # {"id": image.id, "name": image.product_id,"image":image.image}
