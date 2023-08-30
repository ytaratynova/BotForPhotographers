from loader import dp
from aiogram.types import Message

@dp.message_handler()
async def all_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, я не умею работать с командами типа {message.text}')