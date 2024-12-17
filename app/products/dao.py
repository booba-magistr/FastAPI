from fastapi import APIRouter
from sqlalchemy import select
from app.database import session_maker
from app.products.models import Product


router = APIRouter(prefix='/product', tags=['Товары'])