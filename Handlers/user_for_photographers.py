from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_for_photographers, create_ikb_video, create_ikb_presets, create_ikb_product_details
from Keyboards.Callback import main_menu, for_photographers


@dp.callback_query_handler(main_menu.filter(button='for_selling'))
async def for_selling(call: CallbackQuery):
    name = call.from_user.first_name
    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = f'{name}, выбери интересующий тебя продукт:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_photographers())

@dp.callback_query_handler(for_photographers.filter(menu='for_photographers'))
async def video(call: CallbackQuery):
    if call.data.split(':')[-1] == 'video':
        cur_button = "Видеоурок"
    else:
        cur_button = "Пресет"
    video_list = [video[1] for video in product_db.select_product(cur_button)]
    if len(video_list) != 0:
        poster = main_poster.select_poster()[0]
        cur_chat = call.from_user.id
        cur_message = call.message.message_id
        caption = f'Перечень продуктов в категории "{cur_button}", доступные к покупке (нажми и см. подробности):'
        await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                     chat_id=cur_chat, message_id=cur_message,
                                     reply_markup=create_ikb_video(cur_button))
    else:
        await call.answer('Продуктов в данной категории пока нет!')


@dp.callback_query_handler(for_photographers.filter(menu='video_or_preset'))
async def select_package(call: CallbackQuery):
    product_name = call.data.split(':')[-1]
    photo = product_db.select_photo(product_name)[0][0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = f'{product_name}⬆️'
    await bot.edit_message_media(media=InputMediaPhoto(media=photo, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_product_details())


