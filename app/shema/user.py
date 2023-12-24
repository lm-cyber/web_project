from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
