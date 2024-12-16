from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Text, ForeignKey, DOUBLE_PRECISION


class Product(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='CASCADE'))
    name: Mapped[str] = mapped_column(String(130), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(6, 2))
    weight: Mapped[int]

    category: Mapped['Category'] = relationship(backref='product')


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))