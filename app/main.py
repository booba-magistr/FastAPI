from fastapi import FastAPI
import uvicorn
from products.router import product_router
from category.router import category_router
from users.router import user_router
from pages.router import front_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get('/')
def test():
    return {'status': 'success'}


app.include_router(product_router)
app.include_router(category_router)
app.include_router(user_router)
app.include_router(front_router)
# настройка приложение FastAPI для обслуживания стат. файлов 
# '/static'- путь по которому будут доступны стат. файлы(http://localhost:8000/static/test.png) 
app.mount('/static', StaticFiles(directory='app/static'), 'static')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)