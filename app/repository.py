import sqlite3
import sqlalchemy as sa
from contextlib import contextmanager


class PetFeedingRepository:

    def __init__(self,session):
        self.session = session


    def insert(self,feeding):
        ...
    
    def list_all(self):
        ...

    def search_by_id(self,id:int):
        ...

    def update(self,id:int):
        ...

    def delete_by_id(self,id:int):
        ...

    

if __name__ ==  '__main__':
    repo = PetFeedingRepository()
    with repo.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM PetFeeding')
        print(cursor.fetchall())
