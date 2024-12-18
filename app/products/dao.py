from products.models import Product
from dao.base import BaseDAO
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import session_maker


class ProductDAO(BaseDAO):
    model = Product

    @classmethod
    async def get_category(cls, product_id:int):
        async with session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.category)).filter_by(id=product_id)
            result = await session.execute(query)
            product_category = result.scalar_one_or_none()

            if product_category is None:
                return None
            
            product_info = product_category.to_dict()
            product_info['category'] = product_category.name
            return product_info
