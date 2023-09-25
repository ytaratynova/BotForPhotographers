from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_for_photographers, create_ikb_video, create_ikb_presets
from Keyboards.Callback import main_menu, for_photographers


@dp.callback_query_handler(main_menu.filter(button='for_selling'))
async def for_selling(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Выбери интересующий тебя продукт:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_photographers())

@dp.callback_query_handler(for_photographers.filter(button='video'))
async def video(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    video_list = [video[2] for video in product_db.select_product(cur_button)]
    if len(video_list) != 0:
        poster = main_poster.select_poster()[0]
        cur_chat = call.from_user.id
        cur_message = call.message.message_id
        caption = 'Видеоуроки, доступные к покупке:'
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=cur_chat, message_id=cur_message,
                                     reply_markup=create_ikb_video(cur_button))
    else:
        await call.answer('Здесь пока нет видеоуроков к покупке!')


@dp.callback_query_handler(for_photographers.filter(button='presets'))
async def presets(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    presets_list = [preset[2] for preset in product_db.select_product(cur_button)]
    if len(presets_list) != 0:
        poster = main_poster.select_poster()[0]
        cur_chat = call.from_user.id
        cur_message = call.message.message_id
        caption = 'Пресеты, доступные к покупке:'
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=cur_chat, message_id=cur_message,
                                     reply_markup=create_ikb_presets(cur_button))
    else:
        await call.answer('Здесь пока нет пресетов к покупке!')