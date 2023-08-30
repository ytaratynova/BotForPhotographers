from .db_config import DataBase


class User(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (tg_id INTEGER PRIMARY KEY, name VARCHAR, alerts_sale INTEGER, alerts_new_product Integer)'''
        self.execute(sql, commit=True)

    # def create_table_admins(self):
    #     sql = '''CREATE TABLE IF NOT EXISTS admins
    #             (admin_id INTEGER PRIMARY KEY, tg_id INTEGER, active INTEGER)'''
    #     self.execute(sql, commit=True)

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
        # sql = f'''SELECT alerts_{option} FROM users WHERE tg_id=?'''
        # return self.execute(sql, (tg_id,), fetchone=True)


    # def select(self, **kwargs):
    #     sql = '''SELECT tg_id FROM users_options WHERE '''
    #     sql, parameters = self.extract_kwargs(sql, kwargs)
    #     return self.execute(sql, parameters, fetchall=True)
    #
    # def at_course(self, **kwargs):
    #     alert = kwargs.get('alert')
    #     table = kwargs.get('table')
    #     if not table:
    #         sql = f'''SELECT tg_id FROM users_options WHERE {alert}=1'''
    #         return self.execute(sql, fetchall=True)
    #     sql = f'''SELECT users.tg_id FROM users JOIN users_options ON users.tg_id = users_options.tg_id WHERE users_options.{alert}=1 AND users.courses LIKE "%{table}%"'''
    #     return self.execute(sql, fetchall=True)
    #
    #
    # def switch_admin(self, tg_id: int):
    #     sql = f'''UPDATE admins SET active = CASE WHEN active = 1
    #     THEN 0 ELSE 1 END WHERE tg_id=?'''
    #     self.execute(sql, (tg_id,), commit=True)
    #     sql = f'''SELECT active FROM admins WHERE tg_id=?'''
    #     return self.execute(sql, (tg_id,), fetchone=True)
    #
    # def is_admin(self, tg_id: int) -> int:
    #     sql = '''SELECT active FROM admins WHERE tg_id=?'''
    #     return self.execute(sql, (tg_id,), fetchone=True)
