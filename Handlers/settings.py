from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_settings
from Keyboards.Callback import main_menu
import config

@dp.callback_query_handler(main_menu.filter(button='settings'))
async def my_settings(call: CallbackQuery):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    my_set = user_db.settings(cur_chat)
    caption = 'Тут ты можешь изменить настройки оповещений:'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))

@dp.callback_query_handler(main_menu.filter(menu='settings'))
async def select_settings(call: CallbackQuery):
    cur_button = call.data.split(':')[-1]
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    caption = 'Это твои настройки'
    user_db.switch_alert(cur_chat, cur_button)
    my_set = user_db.settings(cur_chat)
    match cur_button:
        case 'sale':
            caption = f'Оповещения об акционных предложениях на съемку: {"ВКЛЮЧЕНЫ" if my_set[2] == 1 else "ОТКЛЮЧЕНЫ" }'
        case 'new_product':
            caption = f'Оповещения о выходе новых уроков и пресетов: {"ВКЛЮЧЕНЫ" if my_set[3] == 1 else "ОТКЛЮЧЕНЫ"}'
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_settings(my_set))