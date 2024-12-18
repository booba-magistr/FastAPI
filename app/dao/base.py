from sqlalchemy import select
from database import session_maker
from products.models import Category


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            products = await session.execute(query)
            result = products.scalars().all()
            return result
        
    @classmethod
    async def get_one_or_nothing(cls, product_id:int):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=product_id)
            product = await session.execute(query)
            result = product.scalar_one_or_none()
            return result
    