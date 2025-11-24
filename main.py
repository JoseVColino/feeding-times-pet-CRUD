from app.database import init_db, get_session
from app.repository import PetFeedingRepository
from app.service import PetFeedingService
from datetime import datetime

def list_all():
    return service.list_all()

def search_by_id():
    id = input('insert the ID: ')
    return service.search_by_id(id)
        

def insert():
    pet_name = input("pet's name (mandatory): ")
    person_name = input("feeder's name (optional): ")
    amount_serving = input("how many servings(optional): ")
    time_feeding = input("when? (YYYY-MM-DD HH:MM:SS): ")
    return service.insert(pet_name,person_name,amount_serving,time_feeding)

def update():
    id = input('ID of entry to update')
    pet_name = input("pet's name (mandatory): ")
    person_name = input("feeder's name (optional): ")
    amount_serving = input("how many servings(optional): ")
    time_feeding = input("when? (YYYY-MM-DD HH:MM:SS): ")
    return service.update(id,pet_name,person_name,amount_serving,time_feeding)

def delete_by_id():
    id = input('insert the ID: ')
    return service.delete_by_id(id)

if __name__ == '__main__':
    init_db()
    while True:
        with get_session() as session:
            repo = PetFeedingRepository(session)
            service = PetFeedingService(repo)
            menu = [
                f'{"":#^30}',
                f'{"PET FEEDING":-^30}',
                f'{"":#^30}',
                '',
                '1- List Feedings',
                '2- Search by ID',
                '3- Add New Feeding',
                '4- Update Entry',
                '5- Delete Entry',
                'x- Exit App'
                ]
            
            choices = {
                '1': list_all,
                '2': search_by_id,
                '3': insert,
                '4': update,
                '5': delete_by_id,
                'x': None 
            }

            print(*menu,sep='\n')
            user_input = input('Choose: ')
            
            if user_input == 'x':
                break

            if user_input in choices.keys():
                res = choices[user_input]()
                print(res)