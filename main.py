import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from database import init_db

from handlers import *

logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()
    
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    dp.include_router(start_router)
    dp.include_router(pagination_router)
    dp.include_router(qr_router)
    dp.include_router(my_tools_router)
    dp.include_router(objects_router)
    dp.include_router(requests_router)
    dp.include_router(help_router)
    dp.include_router(admin_router)
    
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())