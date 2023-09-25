from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import config
from Keyboards.Callback import price_menu_details, price_menu


def create_ikb_package_details(package_id):
    ikb_package_details = InlineKeyboardMarkup(row_width=1)

    ibtn_book = InlineKeyboardButton(text='Заказать',
                                     callback_data=price_menu_details.new(menu='price_menu_details', button='order',
                                                                          package=package_id),
                                     url=f'tg://user?id={config.admin_id[0]}')
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=price_menu.new(menu='prices', button='back_prices'))

    if (package_id != ''):
        ibtn_details = InlineKeyboardButton(text='Подробности',
                                            callback_data=price_menu_details.new(
                                                menu='price_menu_details', button='details', package=package_id))
        ikb_package_details.add(ibtn_details)

    ikb_package_details.add(ibtn_book)
    ikb_package_details.add(ibtn_back)
    return ikb_package_details
