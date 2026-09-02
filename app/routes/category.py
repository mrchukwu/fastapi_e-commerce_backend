from fastapi import APIRouter

router = APIRouter(
  prefix="/categories"
)

@router.post("")
def create_category():
  return {
    "message": "Category created successfully"
  }

@router.get("")
def get_categories():
  return {
    "message": "Categories fetched successfully"
  }

@router.get("/{category_id}")
def get_category_by_id(category_id: int):
  return {
    "category_id": category_id,
    "name": "category1",
    "description": "description1"
  }

@router.put("/{category_id}")
def update_category(category_id: int):
  return {
    "message": f"Category {category_id} updated successfully"
  }

@router.delete("/{category_id}")
def delete_category(category_id: int):
  return {
    "message": f"Category {category_id} deleted successfully"
  }