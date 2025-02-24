from fastapi import APIRouter, Request, Depends, UploadFile
import shutil
from fastapi.templating import Jinja2Templates
from products.router import get_products, get_product
from category.router import get_categories
from users.router import get_profile


front_router = APIRouter(prefix='/pages', tags=['Фронт'])
templates = Jinja2Templates(directory='app/templates')

@front_router.get('/products')  # localhost:8000/pages/products
async def get_products_html(request: Request, 
                            products=Depends(get_products),
                            categories=Depends(get_categories)):  # Обязательный параметр request для управления
    # различными функциями (url-генерация и работа с сессиями)
    return templates.TemplateResponse(name='index.html', context={'request': request,
                                                                  'products': products,
                                                                  'categories': categories})

@front_router.post('/add_photo')
async def add_photo(file: UploadFile, img_name: int):
    # webp- сужение фото без потери качества
    with open(f'app/static/images/{img_name}.webp', 'wb+') as photo_obj:
        shutil.copyfileobj(file.file, photo_obj)


@front_router.get('/products/{product_id}')
async def get_product_html(request: Request, product = Depends(get_product)):
    return templates.TemplateResponse(name='product.html', context={'request': request,
                                                                    'product': product})

@front_router.get('/register')
async def register(request: Request):
    return templates.TemplateResponse(name='auth.html', context={'request': request})

@front_router.get('/login/')
async def login_user(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})

@front_router.get('/profile/')
async def get_profile_html(request: Request, user_data = Depends(get_profile)):
    return templates.TemplateResponse(name='profile.html', context={'request': request,
                                                                    'user': user_data})