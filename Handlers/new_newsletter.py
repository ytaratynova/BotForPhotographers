from loader import *
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from Handlers.States import SendNewsletter
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_admin
from Keyboards.Callback import admin_menu

# акционное предложение для клиентов
@dp.callback_query_handler(admin_menu.filter(button='sales_info'), state=None)
async def sales_info(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите текст сообщения:', chat_id=cur_chat, reply_markup=kb_cancel)
    await SendNewsletter.text.set()


@dp.message_handler(state=SendNewsletter.text)
async def new_sales_info(message: Message, state: FSMContext):
    info = message.text
    await state.update_data({'text': message.text})
    data = await state.get_data()
    caption = f"Сообщение об акционных условиях, которое вы хотите разослать:"
    await bot.send_message(chat_id=message.from_user.id, text=caption)
    await bot.send_message(chat_id=message.from_user.id, text=info,
                             reply_markup=ikb_confirm('sms', 'confirm'))
    await SendNewsletter.next()

@dp.callback_query_handler(state=SendNewsletter.confirm)
async def save_new_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        user_list = [user[0] for user in user_db.select_users_for_sales_alerts()]
        for user in user_list:
            await bot.send_message(chat_id=user, text=data.get("text"))
        caption = f'Сообщение " {data.get("text")}" было разослано. Выбери действие:'

    else:
        await call.answer('Отмена')
        caption = f'Сообщение не было разослано. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()


# информация для фотографов
@dp.callback_query_handler(admin_menu.filter(button='new_product_info'), state=None)
async def sales_info(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Введите текст сообщения:', chat_id=cur_chat, reply_markup=kb_cancel)
    await SendNewsletter.text.set()


@dp.message_handler(state=SendNewsletter.text)
async def new_sales_info(message: Message, state: FSMContext):
    info = message.text
    await state.update_data({'text': message.text})
    data = await state.get_data()
    caption = f"Сообщение о новом продукте, которое вы хотите разослать:"
    await bot.send_message(chat_id=message.from_user.id, text=caption)
    await bot.send_message(chat_id=message.from_user.id, text=info,
                             reply_markup=ikb_confirm('sms', 'confirm'))
    await SendNewsletter.next()

@dp.callback_query_handler(state=SendNewsletter.confirm)
async def save_new_album(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        user_list = [user[0] for user in user_db.select_users_for_new_product_alerts()]
        for user in user_list:
            await bot.send_message(chat_id=user, text=data.get("text"))
        caption = f'Сообщение " {data.get("text")}" было разослано. Выбери действие:'

    else:
        await call.answer('Отмена')
        caption = f'Сообщение не было разослано. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_admin())
    await state.reset_data()
    await state.finish()
