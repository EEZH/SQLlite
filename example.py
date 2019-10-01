import sqlite3
from pprint import pprint


conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

query_create_table = '''
    CREATE TABLE USERS
    (id INTEGER PRIMARY KEY
    , name VARCHAR(100) NOT NULL
    , surname VARCHAR(100) NOT NULL
    , age INTEGER
    , email VARCHAR(100)
    , mobile INTEGER)
'''

query_add_user = '''
    INSERT INTO users
    (name, surname, age, email, mobile)
    VALUES (
    "Tedd"
    , "Walkins"
    , 32
    , "TW@gmail.com"
    , 84946515665998
    )   
'''

query_add_users = '''
    INSERT INTO users
    (name, surname, age, email, mobile)
    VALUES
    (?, ?, ?, ?, ?)
'''

data_users = [
    ("Hermions", "Granger", 19, "hermy@gmail.com", 98567985),
    ("Bob", "Smith", 18, "bs@gmail.com", 654987321),
    ("Tom", "Soyer", 21, "soy@mail.ru", 65628784),
    ("Luc", "Skywalker", 25, "Lluk@gmail.com", 6591243)
    ]

query_fetch_all = '''
    SELECT * FROM users
'''

query_fetch_where = '''
    SELECT name FROM users
    WHERE age =21
'''


query_match = '''
    SELECT * FROM users
    WHERE name LIKE "T%T%"
'''

# query_clear = '''
#     TRUNCATE TABLE users
# '''
#
#
# cursor.executemany(query_add_users, data_users)
# result = cursor.fetchmany(3)[-1]
# result = cursor.fetchall()[2]
# pprint(result)
# cursor.execute(query_add_user)
# cursor.executemany(query_add_users, data_users)
# result = cursor.fetchall()
print(result)




# For save changes
conn.commit()
# conn.rollback()









#####################################




# s = '''
#         dfvdfbf
#         fdbfbdfb
#         '''
#
# def func():
#     '''
#     this just test method
#
#     :NONE:
#     '''
#     return
#

# print(help(func))
# print(type(s))