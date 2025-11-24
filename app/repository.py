from sqlalchemy import select
from .model import PetFeeding
from sqlalchemy.orm import Session


class PetFeedingRepository:


    def __init__(self,session:Session):
        self.session = session


    def insert(self,feeding:PetFeeding):
        return self.session.add(feeding)
    
    def list_all(self):
        stmt = select(PetFeeding)
        return self.session.scalars(stmt)

    def search_by_id(self,id:int):
        stmt = select(PetFeeding).where(PetFeeding.id == id)
        return self.session.scalars(stmt)

    def update(self,id:int,newEntry:PetFeeding):
        entry_to_update = self.session.get(PetFeeding,id)
        entry_to_update = newEntry
        return entry_to_update


    def delete_by_id(self,id:int):
        entry_to_delete = self.search_by_id(id).one()
        return self.session.delete(entry_to_delete)

