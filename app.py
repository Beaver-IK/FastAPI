from fastapi import FastAPI


my_app = FastAPI()


@my_app.get('/')
async def root():
    """Индексный эндпоинт."""
    return {'message': 'Авторелоад действительно работает'}
