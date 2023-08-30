from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import portfolio_menu_photos, main_menu
from loader import photos_db

def create_portfolio_navigation(cur_id: int, album: str, admin: bool):
    ikb_navigation = InlineKeyboardMarkup(row_width=2)
    photos_list = photos_db.select_photos(album)

    prev_id = int(cur_id - 1) if cur_id != 0 else int(len(photos_list) - 1)
    next_id = int(cur_id + 1) if cur_id != int(len(photos_list) - 1) else 0

    ibtn_prev = InlineKeyboardButton(text='<<<', callback_data=portfolio_menu_photos.new(menu='photos', button='previous',
                                                                                         album=album, cur_id=prev_id))

    ibtn_next = InlineKeyboardMarkup(text='>>>', callback_data=portfolio_menu_photos.new(menu='photos', button='next',
                                                                                         album=album, cur_id=next_id))
    ibtn_back = InlineKeyboardMarkup(text='Назад',  callback_data=main_menu.new(menu='main', button='portfolio'))
    ibtn_del = InlineKeyboardMarkup(text='Удалить', callback_data=portfolio_menu_photos.new(menu='photos', button='del',
                                                                                             album=album, cur_id=cur_id))


    ikb_navigation.row(ibtn_prev, ibtn_next)
    if admin:
        ikb_navigation.add(ibtn_del)
    ikb_navigation.add(ibtn_back)

    return ikb_navigation