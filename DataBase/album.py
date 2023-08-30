from .db_config import DataBase


class Album(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_album(self):
        sql = '''CREATE TABLE IF NOT EXISTS album 
        (name VARCHAR PRIMARY KEY)'''
        self.execute(sql, commit=True)

    def add_new_album(self, new_album: dict[str, str]):
        album = (new_album.get('name'),)
        sql = '''INSERT INTO album (name) VALUES (?)'''
        self.execute(sql, album, commit=True)

    def create_album_kb(self):
        sql = '''SELECT DISTINCT name FROM album '''
        return self.execute(sql, fetchall=True)

    def del_album(self, album_name: dict[str, str]):
        album = (album_name.get('name'),)
        sql = '''DELETE FROM album WHERE name=?'''
        return self.execute(sql, album, commit=True, fetchall=True)