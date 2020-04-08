import sqlite3
import hashlib


def add_user(user, pwd, _type):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute(
        'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'
        .format(user, pwd, _type))
    conn.commit()
    conn.close()


with open('users.csv', 'r') as file:
    LINES = file.read().splitlines()

for users in LINES:
    (user, _type) = users.split(',')
    print(user)
    print(_type)
    add_user(user, hashlib.md5(user.encode()).hexdigest(), _type)
