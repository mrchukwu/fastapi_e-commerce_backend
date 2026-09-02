from fastapi import APIRouter

router = APIRouter(
  prefix="/orders"
)

@router.post("")
def create_order():
  return {
    "message": "order created"
  }

@router.get("")
def get_orders():
  return {
    "message": "orders fetched successfully"
  }

@router.put("")
def update_order():
  return{
    "message": "order updated successfully"
  }

@router.get("/{order_id}")
def get_order_by_id(order_id:int):
  return{
    "order_id":order_id,
    "message": "order fetched successfully"
  }

@router.delete("/{order_id}")
def delete_order(order_id:int):
  return{
    "order_id":order_id,
    "message": "order deleted successfully"
  }