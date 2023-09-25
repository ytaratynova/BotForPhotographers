from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import product_db

def create_kb_product_names():

    kb_product_names = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    name_list = [product[0] for product in product_db.select_name()]
    for name in name_list:
        btn = KeyboardButton(text=name)
        kb_product_names.add(btn)

    return kb_product_names