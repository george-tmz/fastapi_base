from pydantic_settings import BaseSettings


class Db(BaseSettings):
    DB_HOST: str = '183.66.79.98'
    DB_PORT: str = '3308'
    DB_USER: str = 'root'
    DB_PASSWORD: str = 'XgjG4rrLJ3'
    DB_NAME: str = 'v3_szr'


class Redis(BaseSettings):
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379

Db = Db()
Redis = Redis()