from aiogram import Bot, Dispatcher
from main import main_router

import asyncio

from config import TOKEN

import datetime as dt

from scheduler.asyncio import Scheduler

from update_currency import job



async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    cron = Scheduler()
    cron.cyclic(dt.timedelta(minutes=30), job)
    await dp.start_polling(bot)
    
asyncio.run(main())


