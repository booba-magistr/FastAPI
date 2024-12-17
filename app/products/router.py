from fastapi import APIRouter
from sqlalchemy import select
from database import session_maker
from products.models import Product
from products.dao import ProductDAO


product_router = APIRouter(prefix='/product', tags=['Товары'])


@product_router.get('/', summary='Получить меню')
async def product():
    return await ProductDAO.get_products()