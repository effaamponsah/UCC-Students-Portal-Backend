# This python file will try and take the form present and pass them to users

import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="test",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def name():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ("webmaster@python.org",))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()


def User(email, password):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `users` WHERE `indexnumber`= %s"
            cursor.execute(query, (email,))
            result1 = cursor.fetchone()
            
        with connection.cursor() as cursor:
            query = "SELECT * FROM `users` WHERE `password`= %s"
            cursor.execute(query, (password,))
            result2 = cursor.fetchone()
        # return result1, result2
    finally:
        return result1, result2
        # print("hello")
