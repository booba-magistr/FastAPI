from fastapi import FastAPI
import uvicorn
from products.router import product_router
from category.router import category_router
from users.router import user_router


app = FastAPI()


@app.get('/')
def test():
    return {'status': 'success'}


app.include_router(product_router)
app.include_router(category_router)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)