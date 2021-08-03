import asyncio
import sys
from functools import wraps

import click
import uvicorn

from guard import VERSION
from guard.settings import settings


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(VERSION, "-v", "--version")
@click.pass_context
@coro
async def cli(ctx: click.Context):
    pass


@cli.command(help="Start web server.")
@click.pass_context
def server(ctx: click.Context):
    uvicorn.run(
        app="guard.factory:app",
        host=settings.server_host,
        port=settings.server_port,
        debug=settings.debug,
    )


def main():
    sys.path.insert(0, ".")
    cli()


if __name__ == "__main__":
    main()
