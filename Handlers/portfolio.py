from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_portfolio_navigation, create_ikb_albums
from Keyboards.Callback import main_menu, portfolio_menu, portfolio_menu_photos, admin_menu
import config

@dp.callback_query_handler(main_menu.filter(button='portfolio'))
async def my_portfolio(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Выбери категорию, которую желаешь посмотреть:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_albums())

@dp.callback_query_handler(portfolio_menu.filter(menu='portfolio'))
async def select_package(call: CallbackQuery, admin: bool):
    cur_button = call.data.split(':')[-1]
    photo_list = [photo[0] for photo in photos_db.select_photos(cur_button)]
    if len(photo_list) != 0:
        cur_id = 0
        poster = photo_list[cur_id]
        cur_chat = call.from_user.id
        cur_message = call.message.message_id
        caption = f'Портфолио {cur_button}⬆️'
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=cur_chat, message_id=cur_message,
                                     reply_markup=create_portfolio_navigation(cur_id, cur_button, admin))
    else:
        await call.answer('В данной галерее еще нет фото!')



@dp.callback_query_handler(portfolio_menu_photos.filter(button='previous'))
# @dp.callback_query_handler(admin_menu.filter(button='previous'))
async def select_package(call: CallbackQuery, admin: bool):
    cur_id = int(call.data.split(':')[-1])
    album = call.data.split(':')[-2]
    photo_list = [photo[0] for photo in photos_db.select_photos(album)]
    poster = photo_list[cur_id]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = f'Портфолио {album}⬆️'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_portfolio_navigation(cur_id, album, admin))


@dp.callback_query_handler(portfolio_menu_photos.filter(button='next'))
async def select_package(call: CallbackQuery, admin: bool):
    cur_id = int(call.data.split(':')[-1])
    album = call.data.split(':')[-2]
    photo_list = [photo[0] for photo in photos_db.select_photos(album)]
    poster = photo_list[cur_id]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = f'Портфолио {album}⬆️'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_portfolio_navigation(cur_id, album, admin))

