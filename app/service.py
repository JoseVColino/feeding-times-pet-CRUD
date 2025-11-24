from .repository import PetFeedingRepository
from sqlalchemy.exc import OperationalError,NoResultFound
from datetime import datetime
from .model import PetFeeding

class PetFeedingService:
    def __init__(self, repo:PetFeedingRepository):
        self.repo = repo

    def insert(self, pet_name, person_name = None, amount_servings= None, time_feeding = None):
        person_name = None if person_name == '' else person_name 
        amount_servings = None if amount_servings == '' else amount_servings
        time_feeding = None if time_feeding == '' else time_feeding
        if not pet_name or len(pet_name) < 1 or len(pet_name) > 30:
            return 'pet name must be specified and with length between 1-30'
        
        if person_name is not None:
            if not isinstance(person_name, str) or len(person_name) < 1 or len(person_name) > 30:
                return 'person name must be a specified string with length between 1-30, or left as None'

        validated_amount_servings = None
        if amount_servings is not None:
            try:
                validated_amount_servings = float(amount_servings) 
            except (ValueError, TypeError):
                return 'invalid amount_servings: must be a number'
            
            if validated_amount_servings <= 0: 
                return 'amount_servings must be positive'
        
        validated_time_feeding = None
        if time_feeding is not None:
            time_feeding = time_feeding.strip()
            
            try:
                validated_time_feeding = datetime.strptime(time_feeding, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                try:
                    validated_time_feeding = datetime.fromisoformat(time_feeding.replace(' ', 'T'))
                except ValueError:
                    return "time_feeding must be a valid datetime string (e.g., 'YYYY-MM-DD HH:MM:SS')."

        try:
            new_feeding = PetFeeding(
                pet_name=pet_name,
                person_name=person_name,
                amount_servings=validated_amount_servings, 
                time_feeding=validated_time_feeding 
            )
            
            self.repo.insert(new_feeding)
            return 'Successfully added new entry!' 
            
        except Exception as e:
            return f"Database error during insertion: {e}"
         
    
    def list_all(self):
        try:
            repo_result = self.repo.list_all()
        except OperationalError as e:
            return f'Error with database: {e}'
        except Exception as e:
            return f'Unexpected error: {e}'
        
        if not repo_result:
            return 'No entries, try inserting'
        
        result = []
        for entry in repo_result:
            result.append('-'*30)
            result.append(f'id: {entry.id},pet_name: {entry.pet_name}, person_name: {entry.person_name}, amount_servings: {entry.amount_servings}, time_feeding: {entry.time_feeding}')
        return '\n'.join(result)

    def search_by_id(self, id):
        try:
            id = int(id)
        except Exception as e:
            return 'invalid id, try again'

        try:
            repo_search = self.repo.search_by_id(id).one()
        except NoResultFound as e: 
            return f'entry with id {id} not found, check the id again'
        except Exception as e:
            return f'Unexpected error: {e}'
        
        entry = repo_search
        result = f'id: {entry.id},pet_name: {entry.pet_name}, person_name: {entry.person_name}, amount_servings: {entry.amount_servings}, time_feeding: {entry.time_feeding}'
        return result
    
    def update(self, id, pet_name, person_name, amount_serving, time_serving):
        self.delete_by_id(id)
        return self.insert(pet_name, person_name, amount_serving, time_serving)

    def delete_by_id(self, id):
        try:
            id = int(id)
        except Exception as e:
            return 'invalid id, try again'

        try:
            self.repo.delete_by_id(id)
        except NoResultFound as e: 
            return f'entry with id {id} not found, check the id again'
        except Exception as e:
            return f'Unexpected error: {e}'
        
        return f'succesfully deleted entry with id {id}'