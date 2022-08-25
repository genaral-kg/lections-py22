
from views import *

def main():
    print('Привет, тебе доступны следующие функции: \n\t 1 - ВСЕ ПРОДУКТЫ:\n\t 2 - ПОЛУЧИТЬ ОДИН ПРОДУКТ\n\t 3 - СОЗДАТЬ ПРОДУКТ\n\t 4 - ОБНОВИТЬ ПРОДУКТ\n\t 5 - УДАЛИТЬ')

    choice = input('Введите действие (1,2,3,4,5): ')
    if choice == '1':
        print(list_of_products())
    elif choice == '2':
        print(retrieve_product())
    elif choice == '3':
        print(create_product())
    elif choice == '4':
        print(update_product())
    elif choice == '5':
        print(delete_product())
    else:
        print('Invalid choice!!')
        main()
    
    ask = input('Хотите продолжить\'?(Yes/No)')
    if ask.lower() == 'yes':
        main()
    else:
        print('Пока!')

main()

