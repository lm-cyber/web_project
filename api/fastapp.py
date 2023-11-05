from fastapi import FastAPI
from .product import product_router
from .type_of_product import type_of_product_router
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
app.include_router(product_router)
app.include_router(type_of_product_router)
