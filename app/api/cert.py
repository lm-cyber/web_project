from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session
from shema import User
from auth import current_superuser_user

from db import get_async_session
from models import CertModel, NewCertModel, CertAdded
from crud import cert_crud

cert_router = APIRouter()


@cert_router.get("/cert/{id}", response_model=CertModel)
async def get_cert(id: int, session: AsyncSession = Depends(get_async_session)):
    return await cert_crud.get(session, id)


@cert_router.get("/cert/", response_model=list[CertModel])
async def get_certes(session: AsyncSession = Depends(get_async_session)):
    return await cert_crud.get_all(session)


@cert_router.post("/cert/", response_model=CertAdded)
async def add_cert(
    cert: NewCertModel, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await cert_crud.create(session, cert)


@cert_router.delete("/cert/{id}")
async def delete_cert(
    id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    await cert_crud.delete_cert(session, id)


@cert_router.put("/cert/", response_model=CertAdded)
async def update_cert(
    cert: CertAdded, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_superuser_user)
):
    return await cert_crud.update(session, cert)
