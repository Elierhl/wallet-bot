from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "crypto_bot"
    ENV_NAME: str = "development"
    LOGGER_FILE_PATH: str = "../output.log"

    BOT_TOKEN: str

    CRYPTOCURRENCY_TOKEN: str

    DB_URL: str
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str

    class Config:
        case_sensitive = True


settings: Settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
