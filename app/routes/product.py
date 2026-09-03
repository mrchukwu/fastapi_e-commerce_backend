from app.dependencies import get_pagination
from fastapi import APIRouter, Depends
from app.schemas.product import ProductCreate, ProductResponse

from app.data.product_data import products_list
from app.dependencies import get_store_name

router = APIRouter(
  prefix = "/products"
)


@router.post("")
def create_product(product: ProductCreate, store_name: str = Depends(get_store_name)):
    return {
      "message": "product created", 
      "product": product,
      "store_name": store_name
    }

@router.get("")
def get_products(pagination: dict = Depends(get_pagination)):
  return {
    "message": "product fetched successfully",
    "skip": pagination["skip"],
    "limit": pagination["limit"],
    
  }

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

