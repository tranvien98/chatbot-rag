# global configs
import os

from pydantic_settings import BaseSettings
from pathlib import Path
from tempfile import gettempdir

TEMP_DIR = Path(gettempdir())

class Settings(BaseSettings):
    # GENERAL
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"  # development, production
    LOG_LEVEL: str = "INFO" # DEBUG, INFO, WARNING, ERROR, CRITICAL
    DEBUG: bool = True
    WORKERS: int = 4
    API_V1_STR: str = "/api"
    STORAGE: str = "public"
    LOG_FOLDER: str = os.path.join(STORAGE, "logs/app.log")
    PROJECT_NAME: str = "Agent Platform"
    HOST: str = '0.0.0.0'
    PORT: int = 5055
    DOMAIN_BE: str = "https://###.owllee.io"
    DOMAIN_FE: str = "https://###.owllee.io "
    VERBOSE_CHAIN_LLM: bool = False
    RATE_LIMITS: str = "500/minute"
    PROMETHEUS_DIR: Path = TEMP_DIR / "prom"

    # jwt token config
    JWT_TOKEN_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = "security-secret-key!@#$%^&*202x"

    # MONGO
    MONGO_URI: str = "mongodb://root:admin202x%40@localhost:8817/vien_agent?retryWrites=true&loadBalanced=false&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin"
    MONGO_DB_NAME: str = "vien_agent"

    # REDIS CONFIG
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6372
    REDIS_PASSWORD: str = "Admin202a"
    REDIS_DB_BASE: int = 0
    #
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()