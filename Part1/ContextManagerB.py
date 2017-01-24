#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysql import connector
from mysql.connector import errors


class DBConnection(object):
    def __init__(self, username='root', password='root', db_name='spring'):
        self.username = username
        self.password = password
        self.db_name = db_name

    def __enter__(self):
        # 如果在connect()方法出现错误呢？
        self.connection = connector.connect(user=self.username, password=self.password, database=self.db_name)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__方法捕获的是with语句块内的错误，并非跟在with后面的代码错误(也就是__enter__方法抛出的错误)
        self.connection.close()
        if not exc_type:
            return True
        # 如果with语句块内出现ProgrammingError，他就会打印下面一句话；
        # 如果出现其他错误__exit__方法返回False，即回溯错误信息。
        if exc_type == errors.ProgrammingError:
            print('++++ Connection database error', exc_val)
            return True

        return False

with DBConnection() as conn:
    # 下面两句代码抛出的所有错误都可被__exit__方法所接收
    conn.execute('SELEC')
    print(conn.fetchall())
