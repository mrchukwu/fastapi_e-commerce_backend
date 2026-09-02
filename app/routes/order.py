from fastapi import APIRouter

from app.schemas.order import ResponseOrder, ResponseOrderItem, CustomerAddress, CreateOrder

router = APIRouter(
  prefix="/orders"
)

@router.post("")
def create_order(order:CreateOrder):
  return {
    "message": "order created",
    "order": order
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