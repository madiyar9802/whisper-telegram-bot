import app.keyboard as kb
from os import remove, getenv
from app.audio import speech_recognition
from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

# Загрузка переменных среды из файла .env
load_dotenv()

router = Router()
bot = Bot(token=getenv('TOKEN'))


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Пожалуйста, отправьте голосовое сообщение или аудиофайл для обработки.',
                         reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(
        'Этот бот преобразует аудиозаписи и голосовые сообщения, которые вы отправляете, в текст и отправляет их обратно в чат.')


@router.message(F.audio)
async def handle_audio(message: Message):
    file_id = message.audio.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disc = f"C:\\Users\\Madiyar\\OneDrive\\Рабочий стол\\Рандомные проекты на питоне\\Новый телеграм бот\\app\\{message.message_id}audio.mp3"
    await bot.download_file(file_path, file_on_disc)
    await message.reply(speech_recognition(file_on_disc))
    try:
        await remove(file_on_disc)
    except Exception as ex:
        print(ex)


@router.message(F.voice)
async def handle_audio(message: Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disc = f"{getenv('file_path')}{str(message.message_id)}"
    await bot.download_file(file_path, file_on_disc)
    await message.reply(speech_recognition(file_on_disc))
    try:
        await remove(file_on_disc)
    except Exception as ex:
        print(ex)
