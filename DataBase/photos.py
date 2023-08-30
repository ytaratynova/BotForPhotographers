from .db_config import DataBase


class Photo(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_photos(self):
        sql = '''CREATE TABLE IF NOT EXISTS photos 
        (photo_id INTEGER PRIMARY KEY AUTOINCREMENT, album VARCHAR, photo VARCHAR)'''
        self.execute(sql, commit=True)

    def new_photo(self, new_photo: dict[str, str]):
        new_photo = (new_photo.get('album'), new_photo.get('photo'))
        sql = '''INSERT INTO photos (album, photo) VALUES (?, ?)'''
        self.execute(sql, new_photo, commit=True)

    def select_photos(self, album: str):
        sql = '''SELECT ALL photo FROM photos WHERE album=?'''
        return self.execute(sql, (album,), fetchall=True)

    def select_photo_id(self, cur_id: str):
        sql = '''SELECT ALL photo_id FROM photos WHERE photo=?'''
        return self.execute(sql, (cur_id,), fetchall=True)

    def del_all_album(self, album_name: dict[str, str]):
        album = (album_name.get('name'),)
        sql = '''DELETE FROM photos WHERE album=?'''
        return self.execute(sql, album, commit=True, fetchall=True)

    def del_photo(self, photo_id: int):
        sql = '''DELETE FROM photos WHERE photo_id=?'''
        return self.execute(sql, (photo_id,), commit=True, fetchall=True)
