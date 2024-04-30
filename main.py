import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router

# Загрузка переменных среды из файла .env
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
