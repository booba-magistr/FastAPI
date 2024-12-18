from sqlalchemy import select
from database import session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            products = await session.execute(query)
            result = products.scalars().all()
            return result