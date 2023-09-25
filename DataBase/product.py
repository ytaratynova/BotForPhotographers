from .db_config import DataBase


class Product(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_product(self):
        sql = '''CREATE TABLE IF NOT EXISTS product 
        (type VARCHAR, name VARCHAR PRIMARY KEY, photo VARCHAR)'''
        self.execute(sql, commit=True)

    def new_product(self, new_product: dict[str, str, str]):
        new_product = (new_product.get('type'), new_product.get('name'), new_product.get('photo'))
        sql = '''INSERT INTO product (type, name, photo) VALUES (?, ?, ?)'''
        self.execute(sql, new_product, commit=True)

    def select_product(self, type: str):
        sql = '''SELECT * FROM product WHERE type=?'''
        return self.execute(sql, (type,), fetchall=True)

    def select_photo(self, name: str):
        sql = '''SELECT photo FROM product WHERE name=?'''
        return self.execute(sql, (name,), fetchall=True)

    def select_name(self):
        sql = '''SELECT name FROM product'''
        return self.execute(sql, fetchall=True)

    def del_product(self, product_name: dict[str, str]):
        name = (product_name.get('name'),)
        sql = '''DELETE FROM product WHERE name=?'''
        return self.execute(sql, name, commit=True, fetchall=True)
