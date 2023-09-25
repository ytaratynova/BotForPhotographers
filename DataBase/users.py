from .db_config import DataBase


class User(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (tg_id INTEGER PRIMARY KEY, name VARCHAR, alerts_sale INTEGER, alerts_new_product Integer)'''
        self.execute(sql, commit=True)

    def new_user(self, tg_id: int, user_name: str):
        sql = '''SELECT * FROM users WHERE tg_id=?'''
        if not self.execute(sql, (tg_id,), fetchone=True):
            new_user = (tg_id, user_name, 0, 0)
            sql = '''INSERT INTO users (tg_id, name, alerts_sale, alerts_new_product) VALUES (?, ?, ?, ?)'''
            self.execute(sql, new_user, commit=True)

    def settings(self, tg_id: int):
        sql = '''SELECT * FROM users WHERE tg_id=?'''
        return self.execute(sql, (tg_id,), fetchone=True)

    def switch_alert(self, tg_id: int, option: str) -> tuple:
        sql = f'''UPDATE users SET alerts_{option} = CASE WHEN alerts_{option} = 1
        THEN 0 ELSE 1 END WHERE tg_id=?'''
        self.execute(sql, (tg_id,), commit=True)

    def select_users_for_sales_alerts(self):
        sql = '''SELECT DISTINCT tg_id FROM users WHERE alerts_sale = 1'''
        return self.execute(sql, fetchall=True)

    def select_users_for_new_product_alerts(self):
        sql = '''SELECT DISTINCT tg_id FROM users WHERE alerts_new_product = 1'''
        return self.execute(sql, fetchall=True)


