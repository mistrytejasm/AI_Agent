from fastapi import APIRouter
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.system import router as system_router
from app.api.v1.endpoints.agents import router as agents_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["Health"],)
api_router.include_router(system_router, tags=["System"],)
api_router.include_router(agents_router,tags=["Agents"],)