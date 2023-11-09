from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import service
from db import get_session
from models import ImageModel
from fastapi import File
image_router = APIRouter()


@image_router.get("/image/")
async def get_image(session: Session = Depends(get_session), id: int = None):
    if id:
        image = await service.get_image(session, id)
        with open(image.image, 'rb') as f:
            contents = f.read()
            return ImageModel(id=image.id, image=image.contents)
    images = await service.get_image(session)
    images_data =[]
    for image in images:
        with open(image.image, 'rb') as f:
            contents = f.read()
        images_data.append(ImageModel(id=image.id, image=contents))
    return images_data


@image_router.post("/image/")
async def add_image(id, file_bytes: bytes = File(),session: Session = Depends(get_session)):
    await service.add_image(session, id, file_bytes)
    return {'status':'ok'}#{"id": image.id, "name": image.product_id,"image":image.image}
