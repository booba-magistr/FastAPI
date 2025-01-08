from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from products.router import get_products


front_router = APIRouter(prefix='/pages', tags=['Фронт'])
templates = Jinja2Templates(directory='app/templates')

@front_router.get('/products')  # localhost:8000/pages/products
async def get_products_html(request: Request, products=Depends(get_products)):  # Обязательный параметр request для управления
    # различными функциями (url-генерация и работа с сессиями)
    return templates.TemplateResponse(name='index.html', context={'request': request,
                                                                  'products': products})