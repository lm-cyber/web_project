from fastapi import FastAPI, APIRouter
from .product import product_router
from .type_of_product import type_of_product_router
from .product_image import product_image_router
from .news_image import news_image_router
from .news import news_router

tags_metadata = [
    {"name": "product"},
    {"name": "type_of_product"},
]

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}, openapi_tags=tags_metadata)

app.include_router(product_router, prefix="/api/v1", tags=["product"])
app.include_router(type_of_product_router, prefix="/api/v1", tags=["type_of_product"])
app.include_router(product_image_router, prefix="/api/v1", tags=["product_image"])
app.include_router(news_image_router, prefix="/api/v1", tags=["news_image"])
app.include_router(news_router, prefix="/api/v1", tags=["news"])
