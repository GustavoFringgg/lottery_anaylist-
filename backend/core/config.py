from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:[password]@db.[project-ref].supabase.co:5432/postgres"
    cors_origins: list[str] = ["http://localhost:3000", "https://your-domain.vercel.app"]
    gaii_api_base: str = "https://medium.gaii.ai/api"

    class Config:
        env_file = ".env"


settings = Settings()
