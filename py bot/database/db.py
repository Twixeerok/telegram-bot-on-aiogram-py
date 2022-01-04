import sqlite3

from aiogram.types import message
from bots import dp, bot


def sql():
    global cur, base
    base = sqlite3.connect('database/user.db')
    cur = base.cursor()
    if base:
        print("data base connected ok")
    cur.execute('CREATE TABLE IF NOT EXISTS menu(answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT, answer5 TEXT)')
    base.commit()
    

async def sql_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?);', tuple(data.values()))
        base.commit()
        


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_message(message.from_user.id, f'Пользователь: {ret[0]}\nИзучает: {ret[1]}\nТратит на это: {ret[2]} часов\nИзучает для: {ret[3]}\nНравится ли ему изучать: {ret[4]}')