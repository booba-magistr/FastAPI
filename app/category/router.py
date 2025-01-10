from fastapi import APIRouter
from .dao import CategoryDAO
from .schemas import SchemaCategoryAdd, SchemaCategoryUpdate


category_router = APIRouter(prefix='/category', tags=['Категории'])


@category_router.post('/add/', summary='Add category')
async def add_category(category: SchemaCategoryAdd):
    status = await CategoryDAO.add(**category.dict())

    if status:
        return {'status': 'success', 'category': status}
    return {'status': 'add error'}


@category_router.put('/update/', summary='Update category')
async def update_category(category: SchemaCategoryUpdate):
    status = await CategoryDAO.update(filter_by={'id': category.id},
                                      name=category.name)
    
    if status:
        return {'status': 'success', 'category': category}
    return {'status': 'update error'}


@category_router.delete('/delete/{category_id}', summary='Delete category')  # Без модели, тк тут всего один параметр
async def delete(category_id: int):
    status = await CategoryDAO.delete(id=category_id)

    if status:
        return {'status': 'success', 'message': f'Категория с {category_id} удалена'}
    return {'status': 'delete error'}

@category_router.get('/all_categories')
async def get_categories():
    return await CategoryDAO.get_all()