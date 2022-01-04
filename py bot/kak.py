from aiogram.utils import executor
from bots import dp, bot
from database import db as sqll


from news import newsru
from handlers import client, opros, weath









async def on_start(n):
    print ('Бот запущен')
    newsru.get_firts_news()
    sqll.sql()

    
    client.register(dp)
    weath.register(dp)
    opros.register(dp)
    

    
    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
    