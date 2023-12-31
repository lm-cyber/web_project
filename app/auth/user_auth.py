import uuid

from fastapi_users import FastAPIUsers

from .transport_and_strategy import auth_backend
from .db import User
from .user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
current_superuser_user = fastapi_users.current_user(active=True, superuser=True)
current_active_user = fastapi_users.current_user(active=True)
