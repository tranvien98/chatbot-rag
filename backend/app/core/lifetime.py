import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.databases import init_mongo_db
from app.core.logging_config import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the db
    configure_logging()
    await init_mongo_db()
    logging.info("Startup complete")

    yield
    logging.info("Shutdown complete")