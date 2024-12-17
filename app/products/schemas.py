from pydantic import BaseModel, Field, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)  #pydantic понимаем что работает с аргументами БД
    id: int
    category_id: int = Field(..., description='Id категории')
    name: str = Field(..., max_length=130, description='Имя товара')
    description: str = Field(..., description='Описание товара')
    price: float = Field(..., description='два знака после запятой')
    weight: int = Field(..., description='Целое число в граммах')