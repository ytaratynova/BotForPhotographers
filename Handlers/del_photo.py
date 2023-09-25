from loader import *
from aiogram.types import  CallbackQuery, InputMediaPhoto
from Keyboards import ikb_confirm, create_ikb_admin, create_ikb_albums
from Keyboards.Callback import admin_menu, portfolio_menu_photos, confirm_request
import config


@dp.callback_query_handler(admin_menu.filter(button='del_photo'))
async def del_photo_admin_menu(call: CallbackQuery):
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    poster = main_poster.select_poster()[0]
    caption = 'Выберите название альбома, из которого хотите удалить фотографию:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_albums())


@dp.callback_query_handler(portfolio_menu_photos.filter(button='del'))
async def del_photo(call: CallbackQuery):
    cur_id = int(call.data.split(':')[-1])
    album = call.data.split(':')[-2]
    photos_list = photos_db.select_photos(album)
    poster = photos_list[cur_id][0]
    photo_id = photos_db.select_photo_id(poster)[0][0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Подтвердите удаление фото!'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=ikb_confirm('del_photo', photo_id))

@dp.callback_query_handler(confirm_request.filter(menu='del_photo'))
async def confirm_del_photo(call: CallbackQuery):
    poster = main_poster.select_poster()[0]
    photo_id = call.data.split(':')[-2]
    cur_message = call.message.message_id
    cur_chat = call.from_user.id
    if call.data.split(':')[-1] == 'yes':
        photos_db.del_photo(photo_id)
        caption = f'Фотография была удалена. Выберите действие:'
    else:
        await call.answer('Отмена')
        caption = f'Удаление фото отменено. Выбери действие:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_admin())
