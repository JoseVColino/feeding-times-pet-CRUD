from app.database import init_db, get_session
from app.



if __name__ == '__main__':
    menu = [
        f'{"PET FEEDING"^20}'
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

    print(menu,sep='\n')
    
    



"""
print("\n==== MENU DE JOGOS ====")
        print("1. Listar Jogos")
        print("2. Buscar Jogo por nome")
        print("3. Adicionar Jogo")
        print("4. Editar Jogo")
        print("5. Excluir Jogo")
        print("0. Voltar ao Menu Principal")
"""