from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int

    DB_NAME: str

    DB_USER: str
    DB_PASSWORD: str

    BOT_TOKEN: str
    MANAGER_CHAT_ID: int

    class Config:
        env_file = "backend/.env"


settings = Settings()