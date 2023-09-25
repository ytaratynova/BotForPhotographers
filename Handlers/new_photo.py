from loader import *
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from Handlers.States import NewPhoto
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin, create_kb_album
from Keyboards.Callback import admin_menu
import config


@dp.callback_query_handler(admin_menu.filter(button='new_photo'), state=None)
# @dp.message_handler(commands=['new_photo'], state=None)
async def new_photo_catch(call: CallbackQuery, admin: bool):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название альбома:', chat_id=cur_chat, reply_markup=kb_cancel)
    await NewPhoto.album.set()


@dp.message_handler(state=NewPhoto.album)
async def album_catch(message: Message, state: FSMContext):
    album_list = [album[0] for album in album_db.create_album_kb()]
    if message.text in album_list:
        await state.update_data({'album': message.text})
        await message.answer(text='Загрузите фото:', reply_markup=kb_cancel)
        await NewPhoto.next()
    else:
        await message.answer(text='Выберите название альбома из списка:', reply_markup=create_kb_album())


@dp.message_handler(content_types='photo', state=NewPhoto.photo)
async def photo_catch(message: Message, state: FSMContext):
    await state.update_data({'photo': message.photo[0].file_id})
    data = await state.get_data()
    caption = f"Добавить фото в альбом: {data.get('album')}?"
    await message.answer(text='Подтвердите действие:', reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('photo'), caption=caption,
                         reply_markup=ikb_confirm('course', 'confirm'))
    await NewPhoto.next()


@dp.callback_query_handler(state=NewPhoto.confirm)
async def save_new_package(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        photos_db.new_photo(data)
        caption = 'Фото было добавлено в портфолио. Выбери действие:'
    else:
        await call.answer('Отмена')
        caption = 'Добавление фото отменено. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()

