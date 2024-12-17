from sqlalchemy import select
from database import session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls):
        async with session_maker() as session:
            query = select(cls.model)
            products = await session.execute(query)
            result = products.scalars().all()
            return result