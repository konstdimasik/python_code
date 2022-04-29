import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect('test_server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    login TEXT,
    password TEXT,
    cash BIGINT
)""")
db.commit()


def reg():
    user_login = input('Login: ')
    user_password = input('Password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()
        print('Зарегистрировано!')
    else:
        print('Такой логин уже есть')
        for value in sql.execute("SELECT * FROM users"):
            print(value)


def casino():
    user_login = input('Log in: ')
    number = randint(1, 2)
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Такого логина не существует. Зарегистрируйтесь")
        reg()
    else:
        if number == 1:
            sql.execute(f'UPDATE users SET cash = {1000} WHERE login = "{user_login}"')
            db.commit()
        else:
            print('Вы проиграли!')


def enter():
    for i in sql.execute('SELECT * FROM users'):
        print(i)


def main():
    casino()
    enter()


main()
