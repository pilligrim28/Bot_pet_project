from aiogram import F, Router
from aiogram.filters import  CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.states as st
import app.database.requests as rq

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в консалтинговое агенство "Делоникс"', reply_markup=kb.main)



@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нажал на кнопку ХЕЛП!!!')

@router.message(F.text=='Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data =='t-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию футболок.')

@router.message(Command('register'))
async def register(message: Message, state: st.FSMContext):
    await state.set_state(st.Register.name)
    await message.answer('Введите ваше имя')

@router.message(st.Register.name)
async def register_name(message: Message, state: st.FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(st.Register.age)
    await message.answer('Введите ваш возраст')


@router.message(st.Register.age)
async def register_age(message: Message, state: st.FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(st.Register.number)
    await message.answer('Введите ваш номер телефона', reply_markup=kb.get_number)

@router.message(st.Register.number, F.contact)
async def register_number(message: Message, state: st.FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\n Номер: {data["number"]}')
    await state.clear()
