from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, text
from database import Base


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))
    # server_default- значение на уровне БД, default- на уровне объектов и моделей в Python коде
    # В таком случае значение бы 0 подставлялось в таблицу при добавлении записи, но в самой таблице
    # не отобразилось данная информация
    count: Mapped[int] = mapped_column(server_default=text('0'))

    products: Mapped[list['Product']] = relationship('Product', back_populates='category')