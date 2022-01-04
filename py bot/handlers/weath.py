
from typing import Text, final
from aiohttp.client import request
import pyowm
owm = pyowm.OWM('f894eeda16e5bc412cef550187af1047')
owms = ('f894eeda16e5bc412cef550187af1047')
import requests
from bots import dp, bot
from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from handlers import opros
from key import markups as nav
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Test(StatesGroup):
    w1 = State()
    w2 = State()

#@dp.message_handler(commands=['opros'])
async def weath(message: types.Message):
    global ID
    ID = message.from_user.id
    await message.reply("Введите город")
    await Test.next()
async def weath2(message: types.Message, state: FSMContext):
        smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstrom": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"

        }
        try:
            async with state.proxy() as data:
                data = message.text
            r = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={data}&appid={owms}&units=metric'
            )
            data = r.json()
            #pprint (data)
            weather = data["weather"][0]["main"]
            if weather in smile:
                wd = smile[weather]
            

            cityq = data["name"]
            cur = data["main"]['temp']
            humidity = data["main"]['humidity']
            pressure = data["main"]['pressure']
            wind = data["wind"]['speed']
        
            await message.answer(f'Погода в городе {cityq} сейчас {wd}:\nтемператра {cur} градуса,\nскорость ветра {wind} м/c,\nвлажность {humidity},\nдавление {pressure}')
            await state.finish()
        except:
            await message.answer('Проверьте название')  

async def end(message: types.Message):
    message.answer('dasdasa')
    
   



def register(dp : Dispatcher):
    dp.register_message_handler(weath, commands=['Погода'])
    dp.register_message_handler(weath2, state=Test.w1)


    
    
   