from src.server import Server
from src.config.config import settings
import uvicorn
import os
from distutils import util


server = Server()
app = server.get_app_instance()


if __name__ == "__main__":
    reload = False
    if "DEV" in os.environ:
        reload = bool(
            util.strtobool(os.environ['DEV'])
        )

    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=reload
    )
