from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    postgres_user: str = Field(..., validation_alias="POSTGRES_USER")
    postgres_password: str = Field(..., validation_alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(..., validation_alias="POSTGRES_DB")
    postgres_host: str = Field(..., validation_alias="POSTGRES_HOST")
    postgres_port: int = Field(..., validation_alias="POSTGRES_PORT")

    tz: str = Field("UTC", validation_alias="TZ")
    pool_size: int = Field(10, validation_alias="DB_POOL_SIZE")
    max_overflow: int = Field(20, validation_alias="DB_MAX_OVERFLOW")

    environment: str = Field("DEV", validation_alias="ENV")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def settings_config() -> Settings:
    # noinspection PyArgumentList
    return Settings()
