from sqlalchemy import select
from products.models import Product
from database import session_maker


class ProductDAO:
    @classmethod
    async def get_products(cls):
        async with session_maker() as session:
            query = select(Product)
            products = await session.execute(query)
            result = products.scalars.all()
            return result