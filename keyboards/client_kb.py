from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b3 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard = True, )

kb_client.row(b1, b3)