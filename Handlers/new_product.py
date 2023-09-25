from loader import *
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from Handlers.States import NewProduct
from Keyboards.Standart import kb_cancel
from Keyboards import ikb_confirm, create_ikb_for_photographers_for_admin, create_kb_product
from Keyboards.Callback import main_menu


@dp.callback_query_handler(main_menu.filter(button='add_product'), state=None)
async def new_product_catch(call: CallbackQuery):
    cur_chat = call.from_user.id
    await bot.send_message(text='Что вы планируете добавить: Видеоурок/Пресет?', chat_id=cur_chat, reply_markup=kb_cancel)
    await NewProduct.type.set()


@dp.message_handler(state=NewProduct.type)
async def type_catch(message: Message, state: FSMContext):

    if message.text in ['Видеоурок', 'Пресет']:
        await state.update_data({'type': message.text})
        await message.answer(text='Загрузите название продукта:', reply_markup=kb_cancel)
        await NewProduct.next()
    else:
        await message.answer(text='Выберите из списка:', reply_markup=create_kb_product())


@dp.message_handler(state=NewProduct.name)
async def name_catch(message: Message, state: FSMContext):
    name_list = [product[0] for product in product_db.select_name()]
    if message.text in name_list:
        await message.answer(text='Продукт с таким названием существует. Удалите существующий продукт или придумайте'
                                  'другое название', reply_markup=kb_cancel)
    else:
        await state.update_data({'name': message.text})
        await message.answer(text='Загрузите информационный постер о продукте:', reply_markup=kb_cancel)
        await NewProduct.next()

@dp.message_handler(content_types='photo', state=NewProduct.photo)
async def photo_catch(message: Message, state: FSMContext):
    await state.update_data({'photo': message.photo[0].file_id})
    data = await state.get_data()
    caption = f"Продукт, который вы планируете добавить:\n{data.get('name')}.\nПодтвердите действие:"

    await bot.send_photo(chat_id=message.from_user.id, photo=data.get('photo'), caption=caption,
                         reply_markup=ikb_confirm('video_or_preset', 'confirm'))
    await NewProduct.next()

@dp.callback_query_handler(state=NewProduct.confirm)
async def save_new_package(call: CallbackQuery, state: FSMContext):
    if call.data.split(':')[-1] == 'yes':
        data = await state.get_data()
        product_db.new_product(data)
        caption = f'Продукт {data.get("name")} добавлен. Выбери действие:'
    else:
        await call.answer('Отмена')
        caption = 'Добавление видеоурока/пресета отменено. Выбери действие:'

    await bot.send_photo(chat_id=call.from_user.id, photo=main_poster.select_poster()[0],
                         caption=caption,
                         reply_markup=create_ikb_for_photographers_for_admin())
    await state.reset_data()
    await state.finish()
