from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.logging import configure_logging
from app.middleware.request_context import RequestContextMiddleware

configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(RequestContextMiddleware)
app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "AI Agent Platform Running"
    }