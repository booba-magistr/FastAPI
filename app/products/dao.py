from products.models import Product
from dao.base import BaseDAO


class ProductDAO(BaseDAO):
    model = Product