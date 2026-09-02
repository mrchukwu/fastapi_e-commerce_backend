from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from app.core.config import settings

from app.routes import product, category, order

app = FastAPI(
  title=settings.app_name,
  version=settings.app_version
)


@app.get("/")
def check():
    return {"message": "hello world"}

app.include_router(product.router, prefix=settings.api_prefix)
app.include_router(category.router, prefix=settings.api_prefix)
app.include_router(order.router, prefix=settings.api_prefix)
