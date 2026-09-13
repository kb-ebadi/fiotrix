from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "FioTrix"
    app_version: str = "0.1.0"
    database_url: str = "postgresql+psycopg2://fiotrix:fiotrix@localhost:5432/fiotrix"
    host: str = "0.0.0.0"
    port: int = 8000


settings = Settings()
