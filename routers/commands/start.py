from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from keyboards.start import get_start_kb
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

router = Router()


@router.message(Command("info"))
async def info_cmd(message: types.Message):
    btn1 = InlineKeyboardButton(
        text="github",
        # url="https://github.com/zaebaldev/aiogram_test_bot",
        callback_data="1",
    )
    btn2 = InlineKeyboardButton(
        text="pavel",
        # url="https://t.me/durov",
        callback_data="2",
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [btn1],
            [btn2],
        ]
    )
    await message.answer(
        text="This is test aiogram bot",
        reply_markup=kb,
    )


@router.message(CommandStart())
async def start_cmd(message: types.Message):

    await message.answer(
        text=f"Hi, {message.from_user.full_name} {message.from_user.id}",
        reply_markup=get_start_kb(),
    )
