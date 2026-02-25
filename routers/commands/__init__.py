from aiogram import Router
from .start import router as start_router
from .survey import router as survey_router

router = Router()

router.include_routers(start_router, survey_router)
