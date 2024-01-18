import pymysql
from pymysql.cursors import Cursor

def connect():
    conn = pymysql.connect(host='52.78.125.119', user='mysql', password='1234', db='test', charset='utf8', autocommit=False)
    cusor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cusor

def execute(crud):
    result = None

    def manage(*args):
        nonlocal result
        conn, cursor = connect()
        try:
            result = crud(cursor, *args)
            conn.commit()

        except Exception as e:
            print(e.__str__())
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

        return result

    return manage