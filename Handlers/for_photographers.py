from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from Keyboards import create_ikb_for_photographers_for_admin
from Keyboards.Callback import main_menu



@dp.callback_query_handler(main_menu.filter(button='on_off'))
async def select_settings(call: CallbackQuery):

    poster = main_poster.select_poster()[0]
    cur_chat = call.from_user.id
    cur_message = call.message.message_id
    if_products.switch_if_you_have_products()
    caption = f'Предложения для фотографов теперь: ' \
              f'{"ВКЛЮЧЕНЫ" if if_products.show_if_you_have_products()[0] == 1 else "ОТКЛЮЧЕНЫ" }'

    await bot.edit_message_media(media=InputMediaPhoto(media=poster, caption=caption),
                                 chat_id=cur_chat, message_id=cur_message,
                                 reply_markup=create_ikb_for_photographers_for_admin())