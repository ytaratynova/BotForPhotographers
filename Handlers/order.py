from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup
from Keyboards import  create_ikb_package_details
from Keyboards.Callback import price_menu_details
import config

@dp.callback_query_handler(price_menu_details.filter(button='order'))
async def my_portfolio(call: CallbackQuery):
    package_id = int(call.data.split(':')[-1][2])
    package_name = package_db.select_package_name_by_id(package_id)

    text = f'Здравствуйте! Мне понравилось Ваше портфолио и интересны подробности по пакету {package_name[0][0]}. ' \
           f'Свяжитесь со мной, пожалуйста. '
    caption = f'Сообщение с текстом "{text}" было отправлено фотографу.'

    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    print(cur_chat)
    print(call)

    cur_message = call.message.message_id
    await bot.send_message(chat_id=config.admin_id[0], text=f'id: {str(cur_chat)}\n' + text)
    await bot.get_user_profile_photos(cur_chat)

    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_package_details(''))

