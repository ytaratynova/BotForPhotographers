from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def create_kb_product():

    kb_product = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    btn_video = KeyboardButton(text='Видеоурок')
    btn_presets = KeyboardButton(text='Пресет')

    kb_product.add(btn_video)
    kb_product.add(btn_presets)

    return kb_product