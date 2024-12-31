from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from database import session_maker
from sqlalchemy import update, delete 


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
    async def add(cls, **values):
        async with session_maker() as session:
            async with session.begin():  # Начинается транзакция(группировка операций для выполнения как одной единицы)
                obj = cls.model(**values)  # Создаю объект класса  
                session.add(obj)  # Добавляю экземпляр в сессию
                try:  # Пытаюсь закрепить информацию в БД
                    await session.commit()
                except SQLAlchemyError as exception:  # Открываем транзакцию и пробрасываю исключение дальше
                    await session.rollback()
                    raise exception
                return obj 
            
    @classmethod
    async def update(cls, filter_by, **values):
        async with session_maker() as session:
            async with session.begin():
                query = (
                update(cls.model)  # Создается запрос на обновление данных 
                .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                .values(**values)
                .execution_options(synchronize_session="fetch")  # Для синхронизации состояния сессии с БД после выполнения запроса 
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as exception:
                    await session.rollback()
                    raise exception
                return result.rowcount
