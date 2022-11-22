from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://{YOUR_POSTGRES_USER}:{YOUR_POSTGRES_PASSWORD}@localhost:5432/filmes'
    DBBaseModel = declarative_base()

    class Config():
        case_sensitive = True


settings = Settings() 