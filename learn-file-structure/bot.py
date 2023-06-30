import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import other_handlers, user_handlers


async def main():
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_routers(user_handlers.router, other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if (__name__ == '__main__'):
    asyncio.run(main())
