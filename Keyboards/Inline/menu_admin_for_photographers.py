from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import admin_menu, main_menu
from loader import if_products


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

def create_ikb_for_photographers_for_admin():

    ikb_for_photographers_for_admin = InlineKeyboardMarkup(row_width=1)

    ibtn_on_off = InlineKeyboardButton(text=f'У вас есть предложения для фотографов:'
                                            f' {"Да" if if_products.show_if_you_have_products()[0] == 1 else "Нет"}',
                                       callback_data=main_menu.new(
                                                  menu='admin_menu', button='on_off'))
    ibtn_add_product = InlineKeyboardButton(text='Добавить продукт',
                                           callback_data=main_menu.new(
                                               menu='admin_menu', button='add_product'))
    ibtn_del_product = InlineKeyboardButton(text='Удалить продукт',
                                           callback_data=main_menu.new(
                                               menu='admin_menu', button='del_product'))
    ibtn_back = InlineKeyboardButton(text='Назад',
                                             callback_data=main_menu.new(menu='main', button='admin'))

    ikb_for_photographers_for_admin.add(ibtn_on_off)
    ikb_for_photographers_for_admin.add(ibtn_add_product)
    ikb_for_photographers_for_admin.add(ibtn_del_product)
    ikb_for_photographers_for_admin.add(ibtn_back)
    return ikb_for_photographers_for_admin