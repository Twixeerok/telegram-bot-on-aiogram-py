from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token='Вставить свой токен сюда')
dp = Dispatcher(bot, storage=MemoryStorage())