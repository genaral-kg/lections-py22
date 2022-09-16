from views import *
import json

class Car(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, OrderMixin):
    def start(self):
        choice = input('Добро пожаловать!\nХотите начать работу? Да/Нет: ')
        while choice.lower() == 'да':
            # n\t 1 - ВСЕ ПРОДУКТЫ:\n\t 2 - ПОЛУЧИТЬ ОДИН ПРОДУКТ\n\t 3 - СОЗДАТЬ ПРОДУКТ\n\t 4 - ОБНОВИТЬ ПРОДУКТ\n\t 5 - УДАЛИТЬ'
            print('Привет тебе доступны следующие функции:\n\t1 - ВСЕ ПРОДУКТЫ :\n\t2 - ПОЛУЧИТЬ ОДИН ПРОДУКТ:\n\t3 - СОЗДАТЬ ПРОДУКТ:\n\t4 - ОБНОВИТЬ ПРОДУКТ:\n\t5 - УДАЛИТЬ:\n\t6 - ЗАКАЗАТЬ\n\t7 - ВЫХОД:')
            a = int(input('Выберите действие: (1,2,3,4,5,6,7): '))
            if a == 1: print(super().listing_products())
            elif a == 2: print(super().retrieve_data())
            elif a == 3: print(super().create_product())
            elif a == 4: print(super().update_data())
            elif a == 5: print(super().delete_product())
            elif a == 6: print(super().order_car())
            elif a == 7: 
                print('Благодарим вас за работу!')
                break
            else: print('Такого действия нет!')

a = Car()
a.start()
