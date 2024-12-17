from fastapi import FastAPI
import uvicorn
from products.router import product_router


app = FastAPI()
app.include_router(product_router)


@app.get('/')
def test():
    return {'status': 'success'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)