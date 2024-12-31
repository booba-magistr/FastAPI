from fastapi import APIRouter
from .dao import CategoryDAO
from .schemas import SchemaCategoryAdd, SchemaCategoryUpdate


category_router = APIRouter(prefix='/category', tags=['Категории'])


@category_router.post('/add/')
async def add_category(category: SchemaCategoryAdd):
    status = await CategoryDAO.add(**category.dict())
    if status:
        return {'status': 'success', 'category': status}
    return {'status': 'add error'}

@category_router.put('/update/')
async def update_category(category: SchemaCategoryUpdate):
    status = await CategoryDAO.update(filter_by={'id': category.id},
                                      name=category.name)
    
    if status:
        return {'status': 'success', 'category': category}
    return {'status': 'update error'}