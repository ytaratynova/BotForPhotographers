from aiogram import Bot, Dispatcher
import os
from DataBase import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

memory = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)

db = DataBase()
user_db = User()
package_db = Package()
album_db = Album()
photos_db = Photo()