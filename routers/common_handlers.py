from aiogram import F, Router, types
from config import ADMIN_ID


router = Router()


@router.message(F.text.contains("hello"))
async def hello_handler(message: types.Message):
    await message.answer("hi!")
    # await message.answer(text=message.text)


@router.message((F.from_user.id == ADMIN_ID) & (F.text == "secret"))
async def user_message_handler(message: types.Message):
    await message.answer("secret")


@router.message()
async def echo_handler(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)
    # await message.answer(text=message.text)
