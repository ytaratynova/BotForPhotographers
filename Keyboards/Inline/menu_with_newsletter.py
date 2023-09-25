from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Keyboards.Callback import main_menu
import config

def create_ikb_with_newsletter():

    ikb_with_newsletter = InlineKeyboardMarkup(row_width=1)

    ibtn_order = InlineKeyboardButton(text='Заказать',
                                     callback_data=main_menu.new(menu='newsletter', button='order'),
                                     url=f'tg://user?id={config.admin_id[0]}')

    ibtn_thanks = InlineKeyboardButton(text=f'Спасибо за информацию',
                                        callback_data=main_menu.new(menu='newsletter', button='thanks'))

    ikb_with_newsletter.add(ibtn_order)
    ikb_with_newsletter.add(ibtn_thanks)

    return ikb_with_newsletter