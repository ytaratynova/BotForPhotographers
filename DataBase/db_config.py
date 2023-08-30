import sqlite3


class DataBase:

    def __init__(self, db_path: str = 'D:\geekbrains\Botovodstvo\Taratynova_photo\DataBase\photo_bot_db.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


    # def create_table_package(self):
    #     sql = '''CREATE TABLE IF NOT EXISTS package
    #     (id INTEGER PRIMARY KEY AUTOINCREMENT, package_type VARCHAR, time_shooting VARCHAR,
    #     price INTEGER, photos_quantity INTEGER, photobook_size VARCHAR, photobook_pages INTEGER, description TEXT)'''
    #     self.execute(sql, commit=True)

    # def get_package(self, **kwargs):
    #     sql = '''SELECT * FROM package WHERE'''
    #     sql, parameters = self.extract_kwargs(sql, kwargs)
    #     return self.execute(sql, parameters, fetchall=True)

    @staticmethod
    def extract_kwargs(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key} = ?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()
