from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from keyboards.start import get_start_kb
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from db import cursor, conn

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
async def start_cmd(
    message: types.Message,
):
    name = message.from_user.full_name
    email = f"{name}@email.com"
    greeding = f"Hi, {name} {message.from_user.id}"
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (name, email),
    )
    conn.commit()
    conn.close()
    await message.answer(
        text=greeding,
        reply_markup=get_start_kb(),
    )


@router.message(Command("users"))
async def users_cmd(message: types.Message):
    users = cursor.execute("SELECT username FROM users")
    fetched_users = users.fetchall()
    for user in fetched_users:
        await message.answer(
            text=f"{user[0]}",
        )
