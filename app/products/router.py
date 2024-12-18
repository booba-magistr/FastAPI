from fastapi import APIRouter, Depends
from products.dao import ProductDAO
from .schemas import Product
from products.rb import RBProduct


product_router = APIRouter(prefix='/product', tags=['Товары'])


@product_router.get('/', summary='Получить меню', response_model=list[Product])
async def product(request_body: RBProduct = Depends()):
    # response_model- example value response body
    return await ProductDAO.get_all(**request_body.to_dict())
