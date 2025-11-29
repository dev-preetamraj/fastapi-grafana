import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from src.config.logger import setup_logging
from src.config.settings import Settings

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(json_format=settings.LOG_JSON_FORMAT)
    logger = logging.getLogger("main")
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan, title=settings.APP_NAME)
logger = logging.getLogger("main")

Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Hello World"}
