from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bots import dp
from database import db 
import json
import datetime
from key import markups as nav
from typing import Text, final
from aiohttp.client import request
import requests
import pyowm
owm = pyowm.OWM('f894eeda16e5bc412cef550187af1047')
owms = ('f894eeda16e5bc412cef550187af1047')

#@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Добро пожаловать в мульти бота, выбери действие!", reply_markup=nav.key)
    
    #функция новосетей ##########
#@dp.message_handler()
async def new(message: types.Message):
    if message.text == 'Новости':
        await message.reply('Новости об IT',reply_markup=nav.mainMenu)
    if message.text == 'Контакты':
        await message.reply('Наш инстаграм: \nСоздатель бота: тг-@iiiiemptyhiiii')
        


async def end(message: types.Message):
    await message.answer('dasdasa')
    
    

#@dp.callback_query_handler(text = "btnrandom1")
async def newsone(callback : types.CallbackQuery):
    with open('news/news_dict.json',encoding="utf-8") as file:
        news_dict = json.load(file)
        
    for k, v in sorted(news_dict.items()):
        news = f'{datetime.datetime.fromtimestamp(v["article_date_timestamp"])}\n{v["article_title"]}\n{v["article_desc"]}\n{v["article_url"]}'
        await callback.message.answer(news)
        await callback.answer()

    
#@dp.callback_query_handler(text = "btnrandom_one")
async def newstwo(callback : types.CallbackQuery):
    with open('news/news_dict.json',encoding="utf-8") as file:
        news_dict = json.load(file)
            
    for k, v in sorted(news_dict.items())[-5:]:
        news = f'{datetime.datetime.fromtimestamp(v["article_date_timestamp"])}\n{v["article_title"]}\n{v["article_desc"]}\n{v["article_url"]}'
        await callback.message.answer(news)
        await callback.answer()



def register(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(new)
    dp.register_callback_query_handler(newsone, text = "btnrandom")
    dp.register_callback_query_handler(newstwo, text = "btnrandom_one")
    
    