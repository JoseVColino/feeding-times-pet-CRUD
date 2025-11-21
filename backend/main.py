import sqlite3
from pathlib import Path
from pprint import pprint

if __name__ == '__main__':
    dbpath = Path().cwd()
    print(dbpath)
    with sqlite3.connect('feedings.db') as conn:
        cursor = conn.cursor()
        cursor.execute('select * from petfeeding')
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        pprint([column_names,rows])