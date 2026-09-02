from fastapi import APIRouter

router = APIRouter(
  prefix = "/products"
)

@router.post("")
def create_product():
    return {"message": "product created"}

@router.get("")
def get_products():
  return {
    "message": "Products fetched successfully"
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

