from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import admin_menu, main_menu


def create_ikb_admin():
    ikb_admin = InlineKeyboardMarkup(row_width=1)

    ibtn_change_main = InlineKeyboardButton(text='Обновить главный постер',
                                              callback_data=main_menu.new(
                                                  menu='admin_menu', button='main_poster'))
    ibtn_change_album = InlineKeyboardButton(text='Работа с портфолио',
                                           callback_data=main_menu.new(
                                               menu='admin_menu', button='change_portfolio'))
    ibtn_change_prices = InlineKeyboardButton(text='Работа с пакетами услуг',
                                           callback_data=main_menu.new(
                                               menu='admin_menu', button='change_packages'))
    ibtn_change_for_photographers = InlineKeyboardButton(text='Работа с предложением для фотографов',
                                           callback_data=main_menu.new(
                                               menu='admin_menu', button='change_for_photographers'))
    ibtn_send_msg = InlineKeyboardButton(text='Рассылка',
                                                         callback_data=main_menu.new(
                                                             menu='admin_menu', button='send_info'))
    # ibtn_get_data = InlineKeyboardButton(text='Выгрузить данные',
    #                                      callback_data=main_menu.new(
    #                                          menu='admin_menu', button='get_data'))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                             callback_data=main_menu.new(menu='main', button='back'))

    ikb_admin.add(ibtn_change_main)
    ikb_admin.add(ibtn_change_album)
    ikb_admin.add(ibtn_change_prices)
    ikb_admin.add(ibtn_change_for_photographers)
    ikb_admin.add(ibtn_send_msg)
    # ikb_admin.add(ibtn_get_data)
    ikb_admin.add(ibtn_back)
    return ikb_admin