from typing import List
from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    APP_HOST: str = str(os.environ["BUSINESS_HOST"])
    APP_PORT: int = int(os.environ["BUSINESS_PORT_HOST"])
    SOCKET_PORT_HOST: int = 5000
    DATABASE: str = "pokedex"
    DATABASE_DOCKER_HOST: str = "pokedex-db"
    DATABASE_PORT = 27017
    POKEDEX_COLLECTION: str = "pokedex"
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:4200", "http://0.0.0.0:4200"
    ]
    PROJECT_NAME: str = "Programmers Pokedex"

settings = Settings()
