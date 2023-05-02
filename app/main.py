from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import uvicorn

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

app = FastAPI()

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

    def __hash__(self):  # make class hashable
        return hash((type(self),) + tuple(self.__dict__.values()))

class Request(BaseModel):
    criterion: str
    orders: List[Order]


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    
@cache
@app.post("/solution/")
async def process_orders(request: Request):
    for order in request.orders:
        validate(order)

    filtered_orders = filter(request.orders, request.criterion)
    return sum([order.price * order.quantity for order in filtered_orders])

def filter(orders: List[Order], criterion: str):
    if criterion in ["completed", "pending", "canceled"]:
        return [order for order in orders if order.status == criterion]
    return orders

def validate(order: Order):
    assert isinstance(order.id, int), "Id attribute should be an integer"
    assert order.id >= 0, "Id attribute should be bigger or equal than 0"

    assert isinstance(order.item, str), "Id attribute should be a string"

    assert isinstance(order.quantity, int), "Quantity attribute should be an integer"
    assert order.quantity >= 0, "Quantity attribute should be bigger or equal than 0"

    assert isinstance(order.price, float), "Price attribute should be a float"
    assert order.price >= 0, "Price attribute should be bigger or equal than 0"

    assert isinstance(order.status, str), "Status attribute should be a string"
    assert order.status in ["completed", "pending", "canceled"], "Status attribute should be: completed, cancelled or pending"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
