from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get('/')
def test():
    return {'status': 'success'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)