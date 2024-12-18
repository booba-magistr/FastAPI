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

    category: Mapped['Category'] = relationship('Category', back_populates='products')

    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'weight': self.weight
        }


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))

    products: Mapped[list['Product']] = relationship('Product', back_populates='category')