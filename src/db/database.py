from pymongo import MongoClient
from pymongo.errors import ConnectionFailure  # type: ignore
from src.config.config import settings


class Database(object):
    host: str = ""
    port: int = 0
    dbconn: None = None
    database: None = None

    @staticmethod
    def initialize(
                 host: str = settings.DATABASE_DOCKER_HOST,
                 port: int = settings.DATABASE_PORT):

        Database.host = host
        Database.port = port
        Database.dbconn = None

    @staticmethod
    def connect_to_db():
        try:
            Database.dbconn = MongoClient(
                host=Database.host,
                port=Database.port,
                serverSelectionTimeoutMS=3000
            )
            return Database.check_connection()
        except Exception as err:
            print("ERROR IN DATABASE", err)
            return False

    @staticmethod
    def check_connection():
        try:
            Database.dbconn.admin.command('ismaster')
        except ConnectionFailure:
            return False
        return True

    @staticmethod
    def disconnect_from_db():
        try:
            Database.dbconn.close()
        except Exception:
            return False
        return True

    @staticmethod
    def set_db(database):
        try:
            Database.database = Database.dbconn[database]
        except Exception as err:
            print("Error setting database", err)
            return False
        return True

    @staticmethod
    def get_db():
        try:
            return Database.database
        except Exception:
            return False
