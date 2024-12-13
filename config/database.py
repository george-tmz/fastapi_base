from pydantic_settings import BaseSettings


class Db(BaseSettings):
    DB_HOST: str = ''
    DB_PORT: int = 123
    DB_USER: str = ''
    DB_PASSWORD: str = ''


class Redis(BaseSettings):
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379

Db = Db()
Redis = Redis()