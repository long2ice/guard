from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from guard import settings
from guard.routes import router


def create_app():
    app_ = FastAPI()
    app_.include_router(router)
    register_tortoise(app_, config=settings.TORTOISE_ORM, add_exception_handlers=True)
    return app_


app = create_app()
