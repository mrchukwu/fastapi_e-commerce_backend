from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
  name: str = Field(min_length=3, max_length=100, description="product name")
  price: float = Field(gt=0, description="product price")
  quatity: int = Field(default=0, ge=0)
  description: str | None = Field(default=None, min_length=10, max_length=1000, description="product description")

class ProductResponse(ProductCreate):
  id: int
  name: str
  price: float 
  description: str