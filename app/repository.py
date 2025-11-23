from sqlalchemy import select
from .model import PetFeeding
import sqlalchemy as sa


class PetFeedingRepository:

    def __init__(self,session):
        self.session = session


    def insert(self,feeding):
        ...
    
    def list_all(self):
        stmt = select(PetFeeding)
        result = self.session.scalars(stmt)
        return result

    def search_by_id(self,id:int):
        ...

    def update(self,id:int):
        ...

    def delete_by_id(self,id:int):
        ...

