from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import admin_menu, main_menu


def create_ikb_change_album():
    ikb_change_album = InlineKeyboardMarkup(row_width=1)


    ibtn_new_album = InlineKeyboardButton(text='Добавить новый альбом',
                                           callback_data=admin_menu.new(
                                               menu='change_album', button='new_album'))
    ibtn_del_album = InlineKeyboardButton(text='Удалить альбом и все фото в нем',
                                           callback_data=admin_menu.new(
                                               menu='change_album', button='del_album'))
    ibtn_new_photo = InlineKeyboardButton(text='Добавить фото в альбом',
                                          callback_data=admin_menu.new(
                                              menu='new_photo', button='new_photo'))
    ibtn_del_photo = InlineKeyboardButton(text='Удалить фото из альбома',
                                          callback_data=admin_menu.new(
                                              menu='new_photo', button='del_photo'))

    ibtn_back = InlineKeyboardButton(text='Назад',
                                             callback_data=main_menu.new(menu='main', button='admin'))

    ikb_change_album.add(ibtn_new_album)
    ikb_change_album.add(ibtn_del_album)
    ikb_change_album.add(ibtn_new_photo)
    ikb_change_album.add(ibtn_del_photo)
    ikb_change_album.add(ibtn_back)
    return ikb_change_album