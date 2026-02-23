import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from routers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    print("Bot is starting...")
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
