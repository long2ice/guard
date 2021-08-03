from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from guard import settings
from guard.routes import router


def create_app():
    app = FastAPI()
    app.include_router(router)
    register_tortoise(app, config=settings.TORTOISE_ORM)
    return app
