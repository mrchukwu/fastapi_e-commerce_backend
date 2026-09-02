from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

from app.routes import product, category, order

app = FastAPI()


@app.get("/check")
def check():
    return {"message": "hello world"}

app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)
