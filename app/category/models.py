from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from database import Base


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150))

    products: Mapped[list['Product']] = relationship('Product', back_populates='category')