from loader import *
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from Handlers.States import NewPoster
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin, create_kb_album
from Keyboards.Callback import admin_menu, main_menu



@dp.callback_query_handler(main_menu.filter(button='main_poster'))
async def new_photo_catch(call: CallbackQuery, admin: bool):
    cur_chat = call.from_user.id
    await bot.send_message(text='Загрузити новый постер:', chat_id=cur_chat, reply_markup=kb_cancel)
    await NewPoster.poster.set()


@dp.message_handler(content_types='photo', state=NewPoster.poster)
async def photo_catch(message: Message, state: FSMContext):
    await state.update_data({'poster': message.photo[0].file_id})
    data = await state.get_data()
    caption = f"Изменить стартовый постер на новый?"
    await message.answer(text='Подтвердите действие:', reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster'), caption=caption,
                         reply_markup=ikb_confirm('course', 'confirm'))
    await NewPoster.next()


@dp.callback_query_handler(state=NewPoster.confirm)
async def save_new_package(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        main_poster.new_main_photo(data)
        caption = 'Главный постер был обновлен. Выбери действие:'
    else:
        await call.answer('Отмена')
        caption = 'Главный постер не был изменен. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()
