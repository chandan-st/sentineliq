from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REDIS_URL: str = "redis://localhost:6379"
    OLLAMA_URL: str = "http://127.0.0.1:11434/api/generate"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()