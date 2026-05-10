from fastapi import APIRouter

from app.core.config import settings
from app.core.constants import HEALTH_OK
from app.schemas.health import HealthResponse

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        status=HEALTH_OK,
        service=settings.APP_NAME,
        version=settings.APP_VERSION,
    )