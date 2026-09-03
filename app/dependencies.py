from fastapi import Query

def get_store_name():
  return "FastAPI store"

def get_pagination(limit: int = Query(default=10, le=100), skip: int=Query(default=0, ge=0)):
  return {
    "limit": limit,
    "skip": skip
  }

# 20
# 1 page limit 5
# 2 page limit 5 (skip=5, limit=10)
# 3 page limit 5 (skip=10, limit=15)


def get_sorting(sort_by: str = Query(default="laptop"), order: str = Query(default="asc")):
  return {
    "sort_by": sort_by,
    "order": order
  }