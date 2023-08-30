from loader import dp, db, package_db, bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from Handlers.States import NewPackage
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin
from Keyboards.Callback import admin_menu
import config


# @dp.message_handler(commands=['new_package'], state=None)
# async def new_package_catch(message: Message, admin: bool):
#     if admin:
#         await message.answer(text='Введите название пакета:', reply_markup=kb_cancel)
#         await NewPackage.name.set()
#     else:
#         await message.answer('У вас нет прав для выполнения этой команды!')
#
# @dp.message_handler(state=NewPackage.name)
# async def name_catch(message: Message, state: FSMContext):
#     await state.update_data({'name': message.text})
#     await message.answer(text='Загрузите инфо-постер о пакете:', reply_markup=kb_cancel)
#     await NewPackage.next()
#
#
# @dp.message_handler(content_types='photo', state=NewPackage.poster1)
# async def poster_catch(message: Message, state: FSMContext):
#     await state.update_data({'poster1': message.photo[0].file_id})
#     await message.answer(text='Загрузите подробности о пакете:', reply_markup=kb_cancel)
#     await NewPackage.next()
#
# @dp.message_handler(content_types='photo', state=NewPackage.poster2)
# async def poster_catch(message: Message, state: FSMContext):
#     await state.update_data({'poster2': message.photo[0].file_id})
#     data = await state.get_data()
#     caption = f"Пакет услуг, который вы планируете добавить:\n{data.get('name')}"
#     await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster1'), caption=caption,
#                          reply_markup=ReplyKeyboardRemove())
#     await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster2'), caption='Подтвердите действие:',
#                          reply_markup=ikb_confirm('course', 'confirm'))
#     await NewPackage.next()
#
# @dp.callback_query_handler(state=NewPackage.confirm)
# async def save_new_package(call: CallbackQuery, state: FSMContext):
#     if call.data.split(':')[-1] == 'yes':
#         data = await state.get_data()
#         package_db.add_new_package(data)
#         caption = f'Пакет {data.get("name")} добавлен в перечень услуг. Выбери действие:'
#     else:
#         await call.answer('Отмена')
#         caption = 'Добавление пакета отменено. Выбери действие:'
#
#     await bot.send_photo(chat_id=call.from_user.id, photo=config.start_poster,
#                          caption=caption,
#                          reply_markup=create_ikb_admin())
#     # await bot.send_message(call.message.chat.id, text='Вернуться в главное меню /start')
#     await state.reset_data()
#     await state.finish()

@dp.callback_query_handler(admin_menu.filter(button='new_package'), state=None)
async def new_album_catch(call: CallbackQuery, admin: bool):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название пакета:', chat_id=cur_chat, reply_markup=kb_cancel)
    await NewPackage.name.set()


@dp.message_handler(state=NewPackage.name)
async def name_catch(message: Message, state: FSMContext):
    await state.update_data({'name': message.text})
    await message.answer(text='Загрузите инфо-постер о пакете:', reply_markup=kb_cancel)
    await NewPackage.next()


@dp.message_handler(content_types='photo', state=NewPackage.poster1)
async def poster_catch(message: Message, state: FSMContext):
    await state.update_data({'poster1': message.photo[0].file_id})
    await message.answer(text='Загрузите подробности о пакете:', reply_markup=kb_cancel)
    await NewPackage.next()

@dp.message_handler(content_types='photo', state=NewPackage.poster2)
async def poster_catch(message: Message, state: FSMContext):
    await state.update_data({'poster2': message.photo[0].file_id})
    data = await state.get_data()
    caption = f"Пакет услуг, который вы планируете добавить:\n{data.get('name')}"
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster1'), caption=caption,
                         reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('poster2'), caption='Подтвердите действие:',
                         reply_markup=ikb_confirm('course', 'confirm'))
    await NewPackage.next()

@dp.callback_query_handler(state=NewPackage.confirm)
async def save_new_package(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        package_db.add_new_package(data)
        caption = f'Пакет {data.get("name")} добавлен в перечень услуг. Выбери действие:'
    else:
        await call.answer('Отмена')
        caption = 'Добавление пакета отменено. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=config.start_poster,
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()




