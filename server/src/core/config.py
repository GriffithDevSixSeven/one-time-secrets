from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent.parent.parent/".env"


class DBSettings(BaseSettings):
    POSTGRES_PASSWORD : str
    POSTGRES_USER : str
    POSTGRES_DATABASE : str
    DB_URL : str
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )


db_setting = DBSettings()