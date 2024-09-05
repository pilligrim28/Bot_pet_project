import os
import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main


config=load_dotenv()
TOKEN = os.getenv('TOKEN')






async def main():
    await async_main()
    bot = Bot(token = TOKEN)#Объекты класса
    dp =Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отдыхает')