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
        
    @classmethod
    async def get_category_using_product(cls, product_id:int):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=product_id)
            product = await session.execute(query)
            result = product.scalar_one_or_none()

            if not result:
                return None
            
            query_category = select(Category).filter_by(id=result.category_id)
            category = await session.execute(query_category)
            category_result = category.scalar_one_or_none()

            product_data = result.to_dict()
            product_data['category'] = category_result.name

            return product_data