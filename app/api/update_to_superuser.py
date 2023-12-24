from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_async_session
from shema import User
from auth import current_active_user, current_superuser_user
from werkzeug.security import check_password_hash
from config import PASS_HASH_SUPERUSER

update_superuser_router = APIRouter(tags=["users"])


@update_superuser_router.post("/me_update")
async def update_superuser(
    password: str, user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)
):
    if check_password_hash(PASS_HASH_SUPERUSER, password):
        user.is_superuser = True
        await session.commit()
        return "ok"
    return "wrong password"


@update_superuser_router.post("/disable_superuser")
async def disable_superuser(
    user: User = Depends(current_superuser_user), session: AsyncSession = Depends(get_async_session)
):
    user.is_superuser = False
    await session.commit()
