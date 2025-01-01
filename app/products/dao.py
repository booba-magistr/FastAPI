from category.models import Category
from .models import Product
from dao.base import BaseDAO
from sqlalchemy import select, update, delete, event
from sqlalchemy.orm import joinedload
from database import session_maker


# Событие 'after_insert' - обновляет автоматически счётчик продуктов в таблице Category
@event.listens_for(Product, 'after_insert')
def receive_after_insert(mapper, connection, target):
    category_id = target.category_id
    connection.execute(
        update(Category)
        .where(Category.id == category_id)
        .values(count=Category.count + 1)
    )

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
        
    @classmethod
    async def add_product(cls, **product_data:dict):
        async with session_maker() as session:
            async with session.begin():
                new_product = cls.model(**product_data)
                session.add(new_product)
                await session.flush()
                new_product_id = new_product.id
                await session.commit()
                return new_product_id
