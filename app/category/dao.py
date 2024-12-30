from dao.base import BaseDAO
from .models import Category


class CategoryDAO(BaseDAO):
    model = Category