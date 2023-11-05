from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from db import service
from db import get_session
from models import ProductModel, NewProductModel

product_router = APIRouter()

@product_router.get("/product/", response_model=list[ProductModel] | ProductModel)
async def get_products(session: Session = Depends(get_session), id: int = None):
    if id:
        product = await service.get_product(session, id)
        print(product)
        return ProductModel(id=product.id, name=product.name, type_of_product=product.type_of_product)
    products = await service.get_all_product(session)
    return [ProductModel(id=c.id, name=c.name, type_of_product=c.type_of_product) for c in products]


@product_router.post("/product/")
async def add_product(product: NewProductModel, session: Session = Depends(get_session)):
    print(product.name)
    product = await service.add_product(session, product)
    session.commit()
    return {"id": product.id, "name": product.name}


@product_router.delete("/product/")
async def delete_product(id: int, session: Session = Depends(get_session)):
    await service.delete_product(session, id)
    session.commit()

@product_router.put("/product/")
async def update_product(product: ProductModel, session: Session = Depends(get_session)):
    await service.update_product(session,product)
    session.commit()


