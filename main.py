import uvicorn
from fastapi import FastAPI
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import init_models, service
from db import get_session
from db import ProductModel, ProductOrm, NewProductModel

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/product/", response_model=list[ProductModel]| ProductModel)
async def get_products(session: Session = Depends(get_session), id: int = None):
    if id:
        product = await service.get_product(session, id)
        print(product)
        return ProductModel(id=product.id, name=product.name)
    products = await service.get_all_product(session)
    return [ProductModel(id=c.id, name=c.name) for c in products]


@app.post("/product/")
async def add_product(product: NewProductModel, session: Session = Depends(get_session)):
    print(product.name)
    product = await service.add_product(session, product.name)
    session.commit()
    return {"id": product.id, "name": product.name}


@app.delete("/product/")
async def delete_product(id: int, session: Session = Depends(get_session)):
    await service.delete_product(session, id)
    session.commit()

@app.put("/product/")
async def update_product(product: ProductModel, session: Session = Depends(get_session)):
    await service.update_product(session,product.id, product.name)
    session.commit()



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
