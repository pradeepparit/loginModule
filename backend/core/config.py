import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()  # Load environment variables from .env file

DATABASE_URL = os.getenv("DATABASE_URL")

class Settings(BaseSettings):
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

settings = Settings()
