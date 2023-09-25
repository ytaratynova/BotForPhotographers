from loader import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import DellPackage
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin, create_kb_package
from Keyboards.Callback import admin_menu



@dp.callback_query_handler(admin_menu.filter(button='del_package'), state=None)
async def del_package_catch(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название пакета, который хотите удалить:', chat_id=cur_chat, reply_markup=kb_cancel)
    await DellPackage.name.set()


@dp.message_handler(state=DellPackage.name)
async def name_album(message: Message, state: FSMContext):
    package_list = [package[0] for package in package_db.create_package_kb()]
    if message.text in package_list:
        caption = f"Пакет услуг с названием '{message.text}' будет удален!"
        await state.update_data({'name': message.text})
        await bot.send_message(chat_id=message.from_user.id, text=caption,
                               reply_markup=ikb_confirm('course', 'confirm'))
        await DellPackage.next()
    else:
        await message.answer(text='Выберите название пакета из списка:', reply_markup=create_kb_package())


@dp.callback_query_handler(state=DellPackage.confirm)
async def del_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        package_db.del_package(data)
        caption = f'Пакет {data.get("name")} удален из портфолио. Выбери действие:'
        await call.answer(f'Пакет {data.get("name")} удален!')
    else:
        await call.answer('Отмена')
        caption = f'Пакет услуг НЕ БЫЛ удален! Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()
