from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import message
from bots import dp
from database import db 
import json
import datetime
from key import markups as nav
import requests
owms = ('f894eeda16e5bc412cef550187af1047')




class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()

ID = None

#@dp.message_handler(commands=['opros'])
async def opros(message: types.Message):
    global ID
    ID = message.from_user.id
    await Test.next()
    await message.reply("Как тебя зовут?")
#@dp.message_handler(state=Test.Q1)
async def one(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer1'] = message.text
        await message.reply("Какой язык программирование ты изучаешь?")
        await Test.next()
#@dp.message_handler(state=Test.Q3)
async def two(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer2'] = message.text
        await message.reply("Сколько часов в день ты тратишь?(напишите число)")
        await Test.next()
#@dp.message_handler(state=Test.Q3)
async def three(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer3'] = message.text
        await message.reply(f"Для каких целей вы изучаете {data['answer2']}?")
        await Test.next()
#@dp.message_handler(state=Test.Q3)
async def fore(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer4'] = message.text
        await message.reply("Вам нравился изучать программирование")
        await Test.next()
#@dp.message_handler(state=Test.Q2)
async def fife(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['answer5'] = message.text

        await db.sql_add(state)
        await message.answer('Спасибо за прохождение опроса :)')
        await state.finish()#
        
#@dp.message_handler(commands=['read'])
async def read(message: types.Message):
    await db.sql_read(message)


def register(dp : Dispatcher):
    dp.register_message_handler(opros, commands=['Опрос'])
    dp.register_message_handler(read, commands=['Результаты'])
    dp.register_message_handler(one, state=Test.Q1)
    dp.register_message_handler(two, state=Test.Q2)
    dp.register_message_handler(three, state=Test.Q3)
    dp.register_message_handler(fore, state=Test.Q4)
    dp.register_message_handler(fife, state=Test.Q5)




