from fastapi import APIRouter
from app.schemas.product import ProductCreate, ProductResponse

from app.data.product_data import products_list

router = APIRouter(
  prefix = "/products"
)


@router.post("")
def create_product(product: ProductCreate):
    return {"message": "product created", "product": product}

@router.get("", response_model=list[ProductResponse])
def get_products(products: list[ProductResponse] = products_list):
  return products

@router.get("/{product_id}")
def get_product_by_id(product_id: int):
  return { 
    "product_id":product_id,
    "name": "product1",
    "price": 100,
    "description": "description1"
  }

@router.put("/{product_id}")
def update_product(product_id: int):
  return {
    "message": f"product {product_id} updated successfully"
  }

