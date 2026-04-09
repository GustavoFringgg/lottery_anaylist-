from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/lottery"
    redis_url: str = "redis://localhost:6379"
    cors_origins: list[str] = ["http://localhost:3000", "https://your-domain.vercel.app"]
    gaii_api_base: str = "https://medium.gaii.ai/api"

    class Config:
        env_file = ".env"


settings = Settings()
