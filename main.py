import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("secret")

bot = Bot(token=str(TOKEN))
dp = Dispatcher()


@dp.message(Command("info"))
async def info_cmd(message: types.Message):
    await message.answer("This is test aiogram bot")


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}")


@dp.message()
async def echo_handler(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)
    # await message.answer(text=message.text)


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
