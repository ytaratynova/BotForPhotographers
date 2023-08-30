from .db_config import DataBase


class Package(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_package(self):
        sql = '''CREATE TABLE IF NOT EXISTS package 
        (package_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, poster1 VARCHAR, poster2 VARCHAR)'''
        self.execute(sql, commit=True)

    def add_new_package(self, new_package: dict[str, str, str]):
        package =(new_package.get('name'), new_package.get('poster1'), new_package.get('poster2'))
        sql = '''INSERT INTO package (name, poster1, poster2) VALUES (?, ?, ?)'''
        self.execute(sql, package, commit=True)

    def create_package_kb(self):
        sql = '''SELECT DISTINCT name FROM package '''
        return self.execute(sql, fetchall=True)

    def select_package1(self, package_name: str):
        sql = '''SELECT poster1 FROM package WHERE name=?'''
        return self.execute(sql, (package_name,), fetchall=True)

    def select_package2(self, package_id: int):
        sql = '''SELECT poster2 FROM package WHERE package_id=?'''
        return self.execute(sql, (package_id,), fetchall=True)

    def select_package_id_by_name(self, package_name: str):
        sql = '''SELECT package_id FROM package WHERE name=?'''
        return self.execute(sql, (package_name,), fetchall=True)

    def select_package_name_by_id(self, package_id: int):
        sql = '''SELECT name FROM package WHERE package_id=?'''
        return self.execute(sql, (package_id,), fetchall=True)

    def del_package(self, package_name: dict[str, str]):
        package = (package_name.get('name'),)
        sql = '''DELETE FROM package WHERE name=?'''
        return self.execute(sql, package, commit=True, fetchall=True)
