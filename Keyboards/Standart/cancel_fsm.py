from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_cansel = KeyboardButton(text='Отмена')

kb_cancel.add(btn_cansel)