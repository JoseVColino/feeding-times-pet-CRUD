from app.database import init_db, get_session
from app.repository import PetFeedingRepository
from app.service import PetFeedingService

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
                '1- List Games',
                '2- Search by ID',
                '3- Add New Game',
                '4- Update Game',
                '5- Delete game'
                'x- Exit App'
                ]
            
            choices = {
                '1': service.list_all,
                '2': service.search_by_id,
                '3': service.insert,
                '4': service.update,
                '5': service.delete_by_id,
                'x': None 
            }

            print(*menu,sep='\n')
            user_input = input('Choose: ')
            
            if user_input == 'x':
                break

            if user_input in choices.keys():
                res = choices[user_input]()
                print(res)