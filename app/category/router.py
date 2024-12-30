from fastapi import APIRouter
from .dao import CategoryDAO
from .schemas import SchemaCategoryAdd


category_router = APIRouter(prefix='/category', tags=['Категории'])


@category_router.post('/add/')
async def add_category  (category: SchemaCategoryAdd):
    status = await CategoryDAO.add(**category.dict())
    if status:
        return {'status': 'success', 'category': status}
    return {'status': 'validation error'}