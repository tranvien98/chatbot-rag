import asyncio
import logging
# db connection related stuff
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings

ALL = []

class MongoDBClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = AsyncIOMotorClient(settings.MONGO_URI)
            cls._client.get_io_loop = asyncio.get_running_loop
        return cls._client

    @classmethod
    def get_database(cls):
        return cls.get_client()[settings.MONGO_DB_NAME]


async def init_mongo_db() -> None:
    """
    Create connection pool to database.

    """
    logging.info("Connecting to database")
    client = MongoDBClient.get_client()
    await init_beanie(
        database=client[settings.MONGO_DB_NAME],
        document_models=[model for model in ALL],
    )
    logging.info("Connection to database established")