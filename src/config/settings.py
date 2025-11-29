from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Grafana"
    LOG_JSON_FORMAT: bool = False

    model_config = SettingsConfigDict(env_file=".env")
