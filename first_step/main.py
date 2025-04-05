from fastapi import FastAPI
from pydantic import BaseModel


class Numbers(BaseModel):
    """Класс со слогаемыми и методом вычисления суммы."""

    num1: int
    num2: int

    def get_sum(self):
        """Метод вычисления суммы."""
        return self.num1 + self.num2


app = FastAPI()


@app.post('/calculate')
def calc(nums: Numbers):
    """Эндпоинт для POST запроса вычисления суммы."""
    return {'result': nums.get_sum()}
