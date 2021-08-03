from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool
    db_url: str
    redis_url: str
    server_host: str
    server_port: int

    class Config:
        env_file = ".env"


settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": settings.db_url},
    "apps": {
        "models": {
            "models": ["guard.models"],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}
