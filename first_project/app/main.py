from fastapi import FastAPI

from app.config import CONFIG
from app.logger import LOGGER


app = FastAPI()

if CONFIG.debug:
    app.debug = True
else:
    app.debug = False


@app.get('/')
def read_root():
    """Индексный эндпоинт."""
    return {'message': 'Hello, World!'}


@app.get('/custom')
def read_custom_message():
    """Кастомный эндпоинт."""
    return {'message': 'This is a custom message!'}


@app.get('/db')
def get_db_info():
    """Логгирование подключения к БД."""
    LOGGER.info(f'Connecting to database: {CONFIG.db.database_url}')
