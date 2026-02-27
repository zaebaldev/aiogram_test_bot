import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from routers import router
from aiogram.types.bot_command import BotCommand
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()

log = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
    )
    log.debug(f"token {TOKEN}")
    cmd1 = BotCommand(
        command="/survey",
        description="start survey",
    )
    await bot.set_my_commands(
        commands=[cmd1],
    )
    log.info("Bot is starting...")
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        log.error(e)
