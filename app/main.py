from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from app.core.config import settings

from app.routes import product, category, order

app = FastAPI(
  title=settings.app_name,
  version=settings.app_version
)


@app.get("/app-info")
def app_info():
    return {
      "app_name": settings.app_name,
      "app_version": settings.app_version,
      "admin_email": settings.admin_email,
      "api_prefix": settings.api_prefix,
      "description": "FastAPI Ecommerce Backend",
      "docs": f"{settings.api_prefix}/docs",
      "redoc": f"{settings.api_prefix}/redoc"
    }

app.include_router(product.router, prefix=settings.api_prefix)
app.include_router(category.router, prefix=settings.api_prefix)
app.include_router(order.router, prefix=settings.api_prefix)
