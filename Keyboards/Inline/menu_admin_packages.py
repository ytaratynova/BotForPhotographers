from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import admin_menu, main_menu


def create_ikb_change_packages():
    ikb_change_packages = InlineKeyboardMarkup(row_width=1)


    ibtn_new_package = InlineKeyboardButton(text='Добавить новый пакет услуг',
                                           callback_data=admin_menu.new(
                                               menu='change_album', button='new_package'))
    ibtn_del_package = InlineKeyboardButton(text='Удалить пакет услуг',
                                           callback_data=admin_menu.new(
                                               menu='change_album', button='del_package'))

    ibtn_back = InlineKeyboardButton(text='Назад',
                                             callback_data=main_menu.new(menu='main', button='admin'))

    ikb_change_packages.add(ibtn_new_package)
    ikb_change_packages.add(ibtn_del_package)
    ikb_change_packages.add(ibtn_back)
    return ikb_change_packages