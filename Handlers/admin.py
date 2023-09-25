from loader import *
from aiogram.types import CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_admin, create_ikb_change_album, create_ikb_change_packages, \
    create_ikb_for_mailing_list, create_ikb_for_photographers_for_admin
from Keyboards.Callback import main_menu

# Здесь обрабатываются все CallBack меню администратора, кроме замены главного постера

@dp.callback_query_handler(main_menu.filter(button='admin'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Тебе доступно меню администратора:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_admin())

@dp.callback_query_handler(main_menu.filter(button='change_portfolio'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'В данном меню ты можешь:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_change_album())

@dp.callback_query_handler(main_menu.filter(button='change_packages'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'В данном меню ты можешь:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_change_packages())

@dp.callback_query_handler(main_menu.filter(button='send_info'))
async def send_info(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Желаешь сделать рассылку:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_mailing_list())

@dp.callback_query_handler(main_menu.filter(button='change_for_photographers'))
async def iam_admin(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'В данном меню ты можешь:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_photographers_for_admin())

