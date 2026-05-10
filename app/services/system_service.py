from app.core.config import settings

class SystemService:
    @staticmethod
    async def get_system_info() -> dict:
        return {
            "app_name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "debug": settings.DEBUG,
        }