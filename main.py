from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    """Индексный эндпоинт."""
    return {'message': 'Hello World'}
