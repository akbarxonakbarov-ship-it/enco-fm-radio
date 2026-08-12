import asyncio

from aiogram import Bot, Dispatcher

from app.config import settings
from app.database.session import init_db
from app.admin_bot.handlers import router


async def main() -> None:
    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_router(router)

    print("Enco FM Database Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
