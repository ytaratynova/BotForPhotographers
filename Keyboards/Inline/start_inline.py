import callback as callback
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu

def ikb_start(admin: bool):
    ikb_start = InlineKeyboardMarkup(row_width=1)

    if admin:
        ibtn_admin = InlineKeyboardButton(text='Администрирование',
                                          callback_data=main_menu.new(
                                              menu='main', button='admin'))
        ikb_start.add(ibtn_admin)


    ibtn_portfolio = InlineKeyboardButton(text='Портфолио',
                                     callback_data=main_menu.new(
                                            menu='main', button='portfolio'))
    ibtn_prices = InlineKeyboardButton(text='Услуги и цены',
                                   callback_data=main_menu.new(
                                       menu='main', button='prices'))
    ibtn_settings = InlineKeyboardButton(text='Настройки',
                                     callback_data=main_menu.new(
                                         menu='main', button='settings'))
    ibtn_for_selling = InlineKeyboardButton(text='Предложения для фотографов',
                                        callback_data=main_menu.new(
                                            menu='main', button='for_selling'))

    ikb_start.add(ibtn_portfolio)
    ikb_start.add(ibtn_prices)
    ikb_start.add(ibtn_for_selling)
    ikb_start.add(ibtn_settings)
    return ikb_start