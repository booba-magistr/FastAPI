from fastapi import APIRouter, Depends
from .dao import ProductDAO
from .schemas import Product, SchemaProductAdd
from .rb import RBProduct


product_router = APIRouter(prefix='/product', tags=['Товары'])


@product_router.get('/', summary='Get product menu', response_model=list[Product])
async def get_products(request_body: RBProduct = Depends()):
    # response_model- example value response body
    return await ProductDAO.get_all(**request_body.to_dict())


@product_router.get('/{product_id}', summary='Get product using id')
async def get_product(product_id:int):
    result = await ProductDAO.get_one_or_nothing(product_id)
    if result is None:
        return {'message': f'Товар с id:{product_id} не найден'}
    return result


@product_router.post('/add/', summary='Add Product')
async def add_product(product: SchemaProductAdd):
    status = await ProductDAO.add_product(**product.dict())

    if status:
        return {'status': 'success', 'product': product}
    return {'status': 'add error'}


@product_router.delete('/delete/{product_id}')
async def delete_product(product_id:int):
    status = await ProductDAO.delete_product_by_id(product_id=product_id)

    if status:
        return {'status': f'Продукт с id={product_id} удалён'}
    return {'status': 'delete error'}
