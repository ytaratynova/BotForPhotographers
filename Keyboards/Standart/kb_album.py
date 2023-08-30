from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import album_db

def create_kb_album():

    kb_albums = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    album_list = [album[0] for album in album_db.create_album_kb()]
    for album in album_list:
        btn=KeyboardButton(text=album)
        kb_albums.add(btn)

    return kb_albums