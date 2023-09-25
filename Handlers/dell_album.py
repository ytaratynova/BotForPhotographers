from loader import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import DellAlbum
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin, create_kb_album
from Keyboards.Callback import admin_menu
import config


@dp.callback_query_handler(admin_menu.filter(button='del_album'), state=None)
async def del_album_catch(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название альбома:', chat_id=cur_chat, reply_markup=kb_cancel)
    await DellAlbum.name.set()


@dp.message_handler(state=DellAlbum.name)
async def name_album(message: Message, state: FSMContext):
    album_list = [album[0] for album in album_db.create_album_kb()]
    if message.text in album_list:
        caption = f"Альбом с названием '{message.text}' и все фото в нем будут удалены!"
        await state.update_data({'name': message.text})
        await bot.send_message(chat_id=message.from_user.id, text=caption,
                               reply_markup=ikb_confirm('course', 'confirm'))
        await DellAlbum.next()
    else:
        await message.answer(text='Выберите название альбома из списка:', reply_markup=create_kb_album())


@dp.callback_query_handler(state=DellAlbum.confirm)
async def del_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        album_db.del_album(data)
        photos_db.del_all_album(data)
        caption = f'Альбом {data.get("name")} и все фото удалены из портфолио. Выбери действие:'
        await call.answer(f'Альбом {data.get("name")} удален!')
    else:
        await call.answer('Отмена')
        caption = f'Альбом НЕ БЫЛ удален! Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()


