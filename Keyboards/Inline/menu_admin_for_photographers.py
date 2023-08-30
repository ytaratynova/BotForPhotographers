from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import admin_menu, main_menu


def create_ikb_for_mailing_list():
    ikb_for_photographers = InlineKeyboardMarkup(row_width=1)


    ibtn_sales_info = InlineKeyboardButton(text='Инфо об акции на фотосъемку',
                                           callback_data=admin_menu.new(
                                               menu='for_photographers', button='sales_info'))
    ibtn_new_product_info = InlineKeyboardButton(text='Инфо о выходе нового урока/пресета',
                                           callback_data=admin_menu.new(
                                               menu='for_photographers', button='new_product_info'))

    ibtn_back = InlineKeyboardButton(text='Назад',
                                             callback_data=main_menu.new(menu='main', button='admin'))

    ikb_for_photographers.add(ibtn_sales_info)
    ikb_for_photographers.add(ibtn_new_product_info)
    ikb_for_photographers.add(ibtn_back)
    return ikb_for_photographers