from aiogram import Router
from .media_handlers import router as media_router
from .common_handlers import router as common_handlers
from .commands import router as commands_router

router = Router()

router.include_routers(
    commands_router,
    media_router,
    common_handlers,
)
