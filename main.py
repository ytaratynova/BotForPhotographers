from Handlers import dp
from aiogram.utils import executor
from loader import db, user_db, package_db, album_db, photos_db
import MiddleWare


async def on_start(_):
    try:
        user_db.create_table_users()
        package_db.create_table_package()
        album_db.create_table_album()
        photos_db.create_table_photos()

        print('DB connected... ok!')
    except IOError:
        print('DB failure!')
    print('Бот запущен!')

if __name__ == '__main__':
    MiddleWare.setup(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)