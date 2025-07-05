# app/core/dependencies.py
import redis.asyncio as redis
from fastapi import Depends
from app.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

async def get_redis():
    return redis_client
