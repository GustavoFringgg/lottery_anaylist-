from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = '.env',env_file_encoding = 'utf-8')
    PROJECT_NAME: str = "Lottery Analysis"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    DATABASE_URL: str
    LAST_NUMBER_URL: str
    NEXT_DRAW_URL: str
    HEADER_USER_AGENT: str
    HEADER_ACCEPT: str
    HEADER_ACCEPT_LANGUAGE: str
    HEADER_REFERER: str

    @property
    def async_database_url(self) -> str:
        return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

settings = Settings()
