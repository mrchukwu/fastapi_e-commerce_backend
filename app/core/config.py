from pydantic import BaseModel
# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  app_name: str
  admin_email: str
  app_version: str
  api_prefix: str
  secret_key: str
  database_url: str
  payment_gateway_secret_key: str

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore"
  )


settings = Settings()