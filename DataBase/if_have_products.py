from .db_config import DataBase


class Products(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_if_products(self):
        sql = '''CREATE TABLE IF NOT EXISTS products
        (product INTEGER)'''
        self.execute(sql, commit=True)

    def show_if_you_have_products(self):
        sql = '''SELECT * FROM products'''
        return self.execute(sql, fetchone=True)

    def switch_if_you_have_products(self):
        sql = f'''UPDATE products SET product = CASE WHEN product = 1
        THEN 0 ELSE 1 END'''
        self.execute(sql, commit=True)