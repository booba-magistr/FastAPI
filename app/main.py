from fastapi import FastAPI
import uvicorn
from products.router import product_router
from category.router import category_router


app = FastAPI()


@app.get('/')
def test():
    return {'status': 'success'}


app.include_router(product_router)
app.include_router(category_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)