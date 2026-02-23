import asyncio
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from config import TOKEN, ADMIN_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("info"))
async def info_cmd(message: types.Message):
    await message.answer("This is test aiogram bot")


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name} {message.from_user.id}")


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("I cant view photo!")


@dp.message(F.text == "hello")
async def hello_handler(message: types.Message):
    await message.answer("hi!")
    # await message.answer(text=message.text)


@dp.message((F.from_user.id == ADMIN_ID) & (F.text == "secret"))
async def user_message_handler(message: types.Message):
    await message.answer("secret")


@dp.message()
async def echo_handler(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)
    # await message.answer(text=message.text)


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
