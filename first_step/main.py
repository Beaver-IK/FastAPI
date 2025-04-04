from fastapi import FastAPI
from pydantic import BaseModel


class Numbers(BaseModel):
    
    num1: int
    num2: int
    
    def get_sum(self):
        return self.num1 + self.num2

app = FastAPI()


@app.post('/calculate')
def calc(nums: Numbers):
    return {'result': nums.get_sum()}