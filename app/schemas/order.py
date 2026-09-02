from pydantic import BaseModel, Field

class OrderItem(BaseModel):
  product_id: int = Field(gt=0)
  quantity: int = Field(gt=0)

class CustomerAddress(BaseModel):
  address_line1: str = Field(min_length=11)
  city: str = Field(min_length=3)
  state: str = Field(min_length=3)
  zip_code: str = Field(min_length=4)
  country: str = Field(min_length=3)


class CreateOrder(BaseModel):
  customer_id: int = Field(gt=0)
  customer_name: str = Field(min_length=1)
  customer_address: CustomerAddress
  order_items: list[OrderItem]

class ResponseOrderItem(BaseModel):
  product_id: int = Field(gt=0)
  quantity: int = Field(gt=0)
  price: float = Field(gt=0)

class ResponseOrder(BaseModel):
  order_id: int = Field(gt=0)
  customer_name: str = Field(min_length=1)
  customer_address: CustomerAddress
  order_items: list[ResponseOrderItem]
  total_amount: float = Field(gt=0)
  order_date: str = Field(min_length=1)
  order_status: str = Field(min_length=1)
  payment_status: str = Field(min_length=1)
