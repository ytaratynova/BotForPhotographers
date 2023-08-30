from .db_config import DataBase


class Photo(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_photos(self):
        sql = '''CREATE TABLE IF NOT EXISTS main_photo 
        (main_photo VARCHAR PRIMARY KEY)'''
        self.execute(sql, commit=True)

    def delete_main_photo(self):
        sql = '''DELETE FROM main_photo'''
        return self.execute(sql, commit=True)


    def new_main_photo(self, new_photo: str):
        self.delete_main_photo()
        new_photo = (new_photo.get('album'), new_photo.get('photo'))
        sql = '''INSERT INTO main_photo (main_photo) VALUES (?)'''
        self.execute(sql, (new_photo,), commit=True)