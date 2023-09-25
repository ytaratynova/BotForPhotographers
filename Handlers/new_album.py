from loader import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import NewAlbum
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin
from Keyboards.Callback import admin_menu


@dp.callback_query_handler(admin_menu.filter(button='new_album'), state=None)
async def new_album_catch(call: CallbackQuery, admin: bool):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название альбома:', chat_id=cur_chat, reply_markup=kb_cancel)
    await NewAlbum.name.set()


@dp.message_handler(state=NewAlbum.name)
async def name_album(message: Message, state: FSMContext):
    album_list = [album[0] for album in album_db.create_album_kb()]
    if message.text in album_list:
        await message.answer(text='Альбом с таким названием существует! Придумайте другое название:', reply_markup=kb_cancel)
    else:
        await state.update_data({'name': message.text})
        data = await state.get_data()
        caption = f"Альбом, который вы планируете добавить в портфолио:\n {data.get('name')}"
        await bot.send_message(chat_id=message.from_user.id, text=caption,
                             reply_markup=ikb_confirm('album', 'confirm'))
        await NewAlbum.next()

@dp.callback_query_handler(state=NewAlbum.confirm)
async def save_new_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        album_db.add_new_album(data)
        caption = f'Альбом {data.get("name")} добавлен в портфолио. Выбери действие:'
        await call.answer(f'Альбом {data.get("name")} добавлен в БД')
    else:
        await call.answer('Отмена')
        caption = f'Новый альбом не был добавлен в портфолио. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()


