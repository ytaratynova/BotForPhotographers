from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu

def create_ikb_settings(my_set: tuple) -> InlineKeyboardMarkup:
    _, _, sale, new_product = my_set

    ikb_settings = InlineKeyboardMarkup(row_width=1)

    ibtn_sale = InlineKeyboardButton(text=f'О скидках на фотосессию: {"ON" if sale == 1 else "OFF"}',
                                         callback_data=main_menu.new(menu='settings', button='sale'))

    ibtn_new_product = InlineKeyboardButton(text=f'О новых продуктах для фотографов: {"ON" if new_product == 1 else "OFF"}',
                                        callback_data=main_menu.new(menu='settings', button='new_product'))

    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='main', button='back'))

    ikb_settings.add(ibtn_sale)
    ikb_settings.add(ibtn_new_product)
    ikb_settings.add(ibtn_back)
    return ikb_settings