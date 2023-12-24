from .schemas import UserCreate, UserRead, UserUpdate
from .transport_and_strategy import auth_backend
from .user_auth import fastapi_users


auth_jwt = fastapi_users.get_auth_router(auth_backend)
auth_reg = fastapi_users.get_register_router(UserRead, UserCreate)
auth_reset = fastapi_users.get_reset_password_router()
auth_verify = fastapi_users.get_verify_router(UserRead)
auth_users = fastapi_users.get_users_router(UserRead, UserUpdate)
