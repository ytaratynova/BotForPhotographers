from loader import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import DellProduct
from Keyboards.Standart import kb_cancel, create_kb_product_names
from Keyboards import ikb_confirm, create_ikb_for_photographers_for_admin
from Keyboards.Callback import main_menu



@dp.callback_query_handler(main_menu.filter(button='del_product'), state=None)
async def del_product_catch(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите название пакета, который хотите удалить:', chat_id=cur_chat, reply_markup=kb_cancel)
    await DellProduct.name.set()


@dp.message_handler(state=DellProduct.name)
async def name_album(message: Message, state: FSMContext):
    name_list = [product[0] for product in product_db.select_name()]
    if message.text in name_list:
        caption = f"Продукт с названием '{message.text}' будет удален!"
        await state.update_data({'name': message.text})
        await bot.send_message(chat_id=message.from_user.id, text=caption,
                               reply_markup=ikb_confirm('course', 'confirm'))
        await DellProduct.next()
    else:
        await message.answer(text='Выберите название продукта из списка:', reply_markup=create_kb_product_names())


@dp.callback_query_handler(state=DellProduct.confirm)
async def del_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        product_db.del_product(data)
        caption = f'Продукт {data.get("name")} удален из базы. Выбери действие:'
        # await call.answer(f'Пакет {data.get("name")} удален!')
    else:
        await call.answer('Отмена')
        caption = f'Продукт НЕ БЫЛ удален! Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_for_photographers_for_admin())
    await state.reset_data()
    await state.finish()
