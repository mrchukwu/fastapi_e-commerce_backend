
from pydantic import BaseModel


class Settings(BaseModel):
  app_name: str = "E-Commerce FastAPI"
  app_version: str = "1.0.0"
  api_prefix: str = "/api/v1"


settings = Settings()