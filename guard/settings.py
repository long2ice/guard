from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="GUARD",
    settings_files=["config.yaml"],
)

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
