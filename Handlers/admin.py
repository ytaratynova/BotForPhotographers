from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_admin, create_ikb_change_album, create_ikb_change_packages, create_ikb_for_mailing_list
from Keyboards.Callback import main_menu
import config

@dp.callback_query_handler(main_menu.filter(button='admin'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Тебе доступно меню администратора:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_admin())

@dp.callback_query_handler(main_menu.filter(button='change_portfolio'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'В данном меню ты можешь:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_change_album())

@dp.callback_query_handler(main_menu.filter(button='change_packages'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'В данном меню ты можешь:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_change_packages())

@dp.callback_query_handler(main_menu.filter(button='send_info'))
async def send_info(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Желаешь сделать рассылку:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_mailing_list())
