from aiogram.types import Message, CallbackQuery, InputMediaPhoto
import config
from loader import *
from DataBase import *
from Keyboards import ikb_start
from Keyboards.Callback import main_menu

@dp.message_handler(commands=['start'])
async def start_command(message: Message, admin: bool):
    name = message.from_user.first_name
    poster = config.start_poster
    cur_chat = message.from_user.id
    cur_message = message.message_id
    user_db.new_user(cur_chat, name)
    description = f'Добро пожаловать, {name}!\nТы общаешься с ботом фотографа Юлии Таратыновой.\n' \
                  f'Не теряйся и жми на кнопки!😉 '
    await bot.send_photo(chat_id=cur_chat, photo=poster, caption=description,
                         reply_markup=ikb_start(admin))

@dp.callback_query_handler(main_menu.filter(button='back'))
async def back_command(call: CallbackQuery, admin: bool):
    name = call.from_user.first_name
    poster = config.start_poster
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    user_db.new_user(cur_chat, name)
    description = f'{name}, ты в главном меню: )) '
    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=description,),
                         chat_id=cur_chat, message_id=cur_message,
                         reply_markup=ikb_start(admin))

# @dp.message_handler(content_types='photo')
# async def start_command(message: Message):
#     print(message)
