from fastapi import FastAPI, Depends, APIRouter
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from .product import product_router
from .type_of_product import type_of_product_router
from .product_image import product_image_router
from .news_image import news_image_router
from .news import news_router
from .autocomplete import autocomplete_router
from .update_to_superuser import update_superuser_router
from .request_for_product import request_for_product_router
from auth import auth_jwt, auth_reg, auth_reset, auth_verify, auth_users
from db.db_connection import init_models
from fastapi.middleware.cors import CORSMiddleware
tags_metadata = [
    {"name": "product"},
    {"name": "type_of_product"},
]

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}, openapi_tags=tags_metadata)



origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost",
    "https://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_models()


api_v1 = APIRouter()

api_v1.include_router(autocomplete_router, prefix="/api/v1", tags=["search"])
api_v1.include_router(request_for_product_router, prefix="/api/v1", tags=["request_for_product"])
api_v1.include_router(update_superuser_router, prefix="/users", tags=["users"])
api_v1.include_router(product_router, prefix="/api/v1", tags=["product"])
api_v1.include_router(type_of_product_router, prefix="/api/v1", tags=["type_of_product"])
api_v1.include_router(product_image_router, prefix="/api/v1", tags=["product_image"])
api_v1.include_router(news_image_router, prefix="/api/v1", tags=["news_image"])
api_v1.include_router(news_router, prefix="/api/v1", tags=["news"])


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

app.include_router(api_v1)
app.mount("/api",api_v1)

app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

