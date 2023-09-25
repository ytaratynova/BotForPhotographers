from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_prices, create_ikb_package_details
from Keyboards.Callback import main_menu, price_menu, price_menu_details
import config


@dp.callback_query_handler(main_menu.filter(button='prices'))
async def my_prices(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Выбери пакет услуг, с которым желаешь ознакомиться:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_prices())

@dp.callback_query_handler(price_menu.filter(button='back_prices'))
async def select_package(call: CallbackQuery):
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Выбери пакет услуг, с которым желаешь ознакомиться:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_prices())


@dp.callback_query_handler(price_menu.filter(menu='prices'))
async def select_package(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    package_id = package_db.select_package_id_by_name(cur_button)
    poster = package_db.select_package1(cur_button)[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = f'Опции пакета {cur_button}⬆️'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster[0], caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_package_details(package_id))

@dp.callback_query_handler(price_menu_details.filter(button='details'))
async def select_package_details(call: CallbackQuery):
    package_id = int(call.data.split(':')[-1][2])
    poster = package_db.select_package2(package_id)[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    package_name = package_db.select_package_name_by_id(package_id)
    caption = f'Подробности пакета {package_name[0][0]}⬆️'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster[0], caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_package_details(''))


