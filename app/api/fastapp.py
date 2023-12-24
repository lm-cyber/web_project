from fastapi import FastAPI, Depends
from starlette.responses import HTMLResponse

from .product import product_router
from .type_of_product import type_of_product_router
from .product_image import product_image_router
from .news_image import news_image_router
from .news import news_router
from .update_to_superuser import update_superuser_router
from .request_for_product import request_for_product_router
from auth import auth_jwt, auth_reg, auth_reset, auth_verify, auth_users
from db.db_connection import init_models
tags_metadata = [
    {"name": "product"},
    {"name": "type_of_product"},
]

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}, openapi_tags=tags_metadata)


@app.on_event("startup")
async def startup_event():
    await init_models()



app.include_router(auth_jwt, prefix="/auth/jwt", tags=["auth"])
app.include_router(
    auth_reg,
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    auth_reset,
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    auth_verify,
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    auth_users,
    prefix="/users",
    tags=["users"],
)


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("frontend/index.html") as content:
        return HTMLResponse(content=content.read(), media_type="text/html")


app.include_router(request_for_product_router, prefix="/api/v1", tags=["request_for_product"])
app.include_router(update_superuser_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/api/v1", tags=["product"])
app.include_router(type_of_product_router, prefix="/api/v1", tags=["type_of_product"])
app.include_router(product_image_router, prefix="/api/v1", tags=["product_image"])
app.include_router(news_image_router, prefix="/api/v1", tags=["news_image"])
app.include_router(news_router, prefix="/api/v1", tags=["news"])
