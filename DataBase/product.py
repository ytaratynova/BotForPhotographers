from .db_config import DataBase


class Product(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_product(self):
        sql = '''CREATE TABLE IF NOT EXISTS product 
        (product_id INTEGER PRIMARY KEY AUTOINCREMENT, type VARCHAR, name VARCHAR, photo VARCHAR)'''
        self.execute(sql, commit=True)

    def new_product(self, new_product: dict[str, str, str]):
        new_product = (new_product.get('type'), new_product.get('name'), new_product.get('photo'))
        sql = '''INSERT INTO product (type, name, photo) VALUES (?, ?, ?)'''
        self.execute(sql, new_product, commit=True)

    def select_product(self, type: str):
        sql = '''SELECT ALL name FROM product WHERE type=?'''
        return self.execute(sql, (type,), fetchall=True)

    # def select_photo_id(self, cur_id: str):
    #     sql = '''SELECT ALL photo_id FROM photos WHERE photo=?'''
    #     return self.execute(sql, (cur_id,), fetchall=True)
    #
    # def del_all_album(self, album_name: dict[str, str]):
    #     album = (album_name.get('name'),)
    #     sql = '''DELETE FROM photos WHERE album=?'''
    #     return self.execute(sql, album, commit=True, fetchall=True)
    #
    # def del_photo(self, photo_id: int):
    #     sql = '''DELETE FROM photos WHERE photo_id=?'''
    #     return self.execute(sql, (photo_id,), commit=True, fetchall=True)
