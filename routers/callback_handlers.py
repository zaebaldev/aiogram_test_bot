from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "1")
async def handle_callback_data1(callback: CallbackQuery):
    await callback.message.answer(
        text="You pressed first button",
    )
    await callback.answer()


@router.callback_query(F.data == "2")
async def handle_callback_data2(callback: CallbackQuery):
    await callback.message.answer(
        text="You pressed second button",
    )
    await callback.answer()
