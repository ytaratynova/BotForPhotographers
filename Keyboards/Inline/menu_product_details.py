from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import config
from Keyboards.Callback import main_menu, for_photographers


def create_ikb_product_details():
    ikb_product_details = InlineKeyboardMarkup(row_width=1)

    ibtn_book = InlineKeyboardButton(text='Заказать',
                                     callback_data=for_photographers.new(menu='for_photographers', button='order'),
                                     url=f'tg://user?id={config.admin_id[0]}')
    ibtn_back = InlineKeyboardButton(text='Назад',
                                     callback_data=main_menu.new(menu='for_photographers', button='for_selling'))


    ikb_product_details.add(ibtn_book)
    ikb_product_details.add(ibtn_back)
    return ikb_product_details
