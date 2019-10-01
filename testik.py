import sqlite3
from pprint import pprint


conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()


#         #     f"""
#         #     INSERT INTO users
#         #     (name, surname, age, email, mobile)
#         #     VALUES(
#         #     "{name}"
#         #     , "{surname}"
#         #     , {age}
#         #     , "{email}"
#         #     , {mobile}
#         # """
# name = "Tomas"
# surname = "Tromps"
# age = 19
# email = "TT@mail.com"
# mobile = 98653214
#
#
# query_add_user = f'''
#     INSERT INTO users
#     (name, surname, age, email, mobile)
#     VALUES (
#     "{name}"
#     , "{surname}"
#     , "{age}"
#     , "{email}"
#     , "{mobile}" )
# '''


# query_max = '''
#     SELECT name, surname, age FROM users
#     WHERE id =11
# '''

query_max = '''
SELECT MAX("id") FROM users
          
'''
cursor.execute(query_max)
result = cursor.fetchone()
id = result[0]
conn.commit()
pprint(id)

query_id_line = f"""
SELECT * FROM users
    WHERE id ={id}
"""
cursor.execute(query_id_line)
user = cursor.fetchone()
pprint(user)

user_str = f"name: {user[1]}; surname: {user[2]}; age: {user[3]}"
print(user_str)
# result1 = cursor.fetchmany(0)