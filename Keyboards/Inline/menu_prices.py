from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu, price_menu
from loader import package_db


# def create_ikb_prices():
#
#     ikb_prices = InlineKeyboardMarkup(row_width=1)
#     package_list = [package[0] for package in package_db.create_package_kb()]
#     for package in package_list:
#         ibtn=InlineKeyboardButton(text=package,
#                                   callback_data=main_menu.new(menu='prices', button=package))
#         ikb_prices.add(ibtn)
#     ibtn_back = InlineKeyboardButton(text='Назад',
#                                      callback_data=main_menu.new(menu='main', button='back'))
#     ikb_prices.add(ibtn_back)
#     return ikb_prices

def create_ikb_prices():

    ikb_prices = InlineKeyboardMarkup(row_width=1)
    package_list = [package[0] for package in package_db.create_package_kb()]
    for package in package_list:
        ibtn=InlineKeyboardButton(text=package,
                                  callback_data=price_menu.new(menu='prices', button=package))
        ikb_prices.add(ibtn)
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))
    ikb_prices.add(ibtn_back)
    return ikb_prices