from .db_config import DataBase


class Poster(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_poster(self):
        sql = '''CREATE TABLE IF NOT EXISTS poster 
        (poster VARCHAR PRIMARY KEY)'''
        self.execute(sql, commit=True)

    def select_poster(self):
        sql = '''SELECT poster FROM poster'''
        return self.execute(sql, fetchone=True)


    def delete_poster(self):
        sql = '''DELETE FROM poster'''
        return self.execute(sql, commit=True)


    def new_main_photo(self, new_poster: str):
        self.delete_poster()
        new_poster = (new_poster.get('poster'))
        sql = '''INSERT INTO poster (poster) VALUES (?)'''
        self.execute(sql, (new_poster,), commit=True)