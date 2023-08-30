from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import package_db

def create_kb_package():

    kb_package = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    package_list = [package[0] for package in package_db.create_package_kb()]
    for package in package_list:
        btn=KeyboardButton(text=package)
        kb_package.add(btn)

    return kb_package