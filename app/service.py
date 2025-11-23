from .repository import PetFeedingRepository
class PetFeedingService:
    def __init__(self, repo:PetFeedingRepository):
        self.repo = repo

    def insert(self, feeding):
        ...
    
    def list_all(self):
        repo_result = self.repo.list_all()

        return repo_result

    def search_by_id(self, id:int):
        ...

    def update(self, id:int):
        ...

    def delete_by_id(self, id:int):
        ...