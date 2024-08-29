from aiogram import F, Router
from aiogram.filters import  CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нажал на кнопку ХЕЛП!!!')

@router.message(F.text=='У меня все супер!')
async def nice(message: Message):
    await message.answer('Я очень рад')
