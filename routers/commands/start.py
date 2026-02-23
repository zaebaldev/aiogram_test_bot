from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from keyboards.start import get_start_kb

router = Router()


@router.message(Command("info"))
async def info_cmd(message: types.Message):
    await message.answer("This is test aiogram bot")


@router.message(CommandStart())
async def start_cmd(message: types.Message):

    await message.answer(
        text=f"Hi, {message.from_user.full_name} {message.from_user.id}",
        reply_markup=get_start_kb(),
    )
