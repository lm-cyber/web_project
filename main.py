import uvicorn
from fastapi import FastAPI
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import init_models, service
from db import get_session
from db import ProductModel, ProductOrm


app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/product/", response_model=list[ProductModel])
async def get_products(session: Session = Depends(get_session)):
    products = await service.get_all_product(session)
    return [ProductModel(name=c.name) for c in products]


@app.post("/product/")
async def add_product(product: ProductModel, session: Session = Depends(get_session)):
    city = service.add_product(session, product.name)
    try:
        session.commit()
        return city
    except IntegrityError as ex:
        session.rollback()
        raise Exception("pizda")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)