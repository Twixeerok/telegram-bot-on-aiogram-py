from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


##################################
mainMenu = InlineKeyboardMarkup(row_width=2)
btnrandom = InlineKeyboardButton(text='Все новости об IT', callback_data='btnrandom')
btnrandom_one = InlineKeyboardButton(text='5 последних новостей об IT', callback_data='btnrandom_one')
mainMenu.insert(btnrandom)
mainMenu.insert(btnrandom_one)
##################################
button1 = KeyboardButton('Новости', callback_data='btnrandom1')
button2 = KeyboardButton('/Погода', callback_data='btnrandom2')
button3 = KeyboardButton('Контакты', callback_data='btnrandom3')
button4 = KeyboardButton('/Результаты', callback_data='btnrandom4')
button5 = KeyboardButton('/Опрос', callback_data='btnrandom5')
key = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2).add(button4, button5).add(button3)
#admin
button_admin = KeyboardButton('Просмотреть')
key_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_admin)
#weath
button7 = KeyboardButton('Посмотреть погоду', callback_data='btnrandom7')
button8 = KeyboardButton('Выход', callback_data='btnrandom8')
key2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button7, button8)




key2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button2)