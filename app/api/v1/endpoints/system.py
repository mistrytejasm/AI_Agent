from fastapi import APIRouter
from app.services.system_service import SystemService

router = APIRouter()

@router.get("/system")
async def get_system_info():
    return await SystemService.get_system_info() 