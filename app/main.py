from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401 — register Task on Base.metadata
from app.config import settings
from app.database import init_db
from app.routers import tasks


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    description="Interactive Swagger UI is at `/docs`. ReDoc is at `/redoc`.",
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(tasks.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
