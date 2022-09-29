from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.db.database import Database
from src.api.api import api_router
from src.config.config import settings
from src.utils.pokedex import insert_pokedex


class Server(object):
    def __init__(self):
        try:
            Database.initialize(
                host=settings.DATABASE_DOCKER_HOST,
                port=settings.DATABASE_PORT
            )
            Database.connect_to_db()
            Database.set_db(settings.DATABASE)
            api = FastAPI(
                title=settings.PROJECT_NAME,
                openapi_url=f"{settings.API_V1_STR}"
            )
            if settings.BACKEND_CORS_ORIGINS:
                api.add_middleware(
                    CORSMiddleware,
                    allow_origins=[
                        str(origin) for origin in settings.BACKEND_CORS_ORIGINS
                    ],
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
                )

            api.include_router(api_router, prefix=settings.API_V1_STR)
            self.app = api
            insert_pokedex()
        except Exception as e:
            print("Error: {}".format(e))

    def get_app_instance(self):
        return self.app
