import sys

from uvicorn.workers import UvicornWorker
from os import environ

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"


class ServerlessUvicornWorker(UvicornWorker):
    def __init__(self, *args, **kwargs):
        if environ.get("CUSTOM_SERVER", None) is None:
            self.CONFIG_KWARGS["server_header"] = False
        else:
            self.CONFIG_KWARGS["headers"] = [("server", environ["CUSTOM_SERVER"])]
        super().__init__(*args, **kwargs)


app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}
