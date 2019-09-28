import sqlite3


class UsersControl:
    def __init__(self, dbname: str=None):
        self.conn = sqlite3.connect(dbname) if dbname else None
        self.cursor = self.conn.cursor() if self.conn else None

    def search_match_users_by_name(self, name: str) -> list:
        self.cursor.execute(
            f'''
            SELECT * from users 
            WHERE name LIKE'{name[0]}%{name[1:]}%'
            '''
        )
        result = self.cursor.fetchall()
        return result

    def search_users_by_age(self, age: int) -> list:
        self.cursor.execute(
            f"""
            SELECT * FROM users
            WHERE age = age
            """
        )
        result = self.cursor.fetchall()
        return result

