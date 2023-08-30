from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu, portfolio_menu
from loader import album_db


def create_ikb_albums():

    ikb_albums = InlineKeyboardMarkup(row_width=1)
    album_list = [album[0] for album in album_db.create_album_kb()]
    for album in album_list:
        ibtn=InlineKeyboardButton(text=album,
                                  callback_data=portfolio_menu.new(menu='portfolio', button=album))
        ikb_albums.add(ibtn)
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))
    ikb_albums.add(ibtn_back)
    return ikb_albums
