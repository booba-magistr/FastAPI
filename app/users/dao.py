from dao.base import BaseDAO
from .models import User
from database import session_maker
from sqlalchemy import select


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    async def get_user_by_email(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()