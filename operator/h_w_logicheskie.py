"""
  По теме: Логические и условные Операторы
"""
"""
1) Создайте программу, которая будет требовать пароль и проверять, содержатся ли в нем только числа, при этом длина пароля не должна быть менее 8 символов . Если все эти условия выполняются, то программа выдает вам сообщение ‘Ваш пароль сохранен’, если же нет - то программа должна указать необходимое условие для сохранения вашего пароля.

Например:
Ввод: Введите пароль: Makers12345
Вывод: Ваш пароль должен хранить только числа

Ввод: Введите пароль: a12345
Вывод: Ваш пароль должен содержать не менее 8 символов
Ваш пароль должен содержать только буквы

"""
'''password = input('Введите пароль:' )
if password.isdigit() and len(password) >= 8:
    print('Ваш пароль сохранен:')

if not password.isdigit():
  print('Ваш пароль должен хранить только числа')
if not len(password) >= 8:
  print('Ваш пароль должен содержать не менее 8 символов')
'''

"""
2) Напишите программу, которая должна рассчитывать средний балл по следующим предметам: математике, английскому языку и литературе. Проходной балл составляет более 69 баллов. Если ученик набрал проходной балл, то ему выдается сообщение о том, что он допущен к экзаменам. Если он не набрал нужное количество баллов, то ему выдается сообщение о том, что у него недопуск к экзаменам.

Например: 
Ввод: Введите свои баллы по математике, английскому языку и литературе через запятую: 78, 90, 67
Вывод: Вы допущены к экзаменам. Ваш средний балл составляет 78.3 

"""
a,b,c = int(input('математика:')), int(input('англ:')),int(input('литература:'))
d = (a + b + c) / 3

if d > 69:
    print('Вы допущены к экзаменам!', d)
else :
     print('Вы не допущены к экзаменам!', d)




"""
3) Напишите мини-игру Камень-Ножницы-Бумага. Вы играете с компьютером. Для этого используйте встроенный модуль random.

Например:
Ввод: Ваш выбор: Камень
Выбор компьютера: Ножницы
Вывод: Вы выиграли!

Ввод: Ваш выбор: Бумага
Выбор компьютера: Ножницы
Вывод: Вы проиграли!
"""
'''
import random
player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
   
if player == 1:
        print("Вы выбрали камень.")  
if player == 2:
        print("Вы выбрали ножницы.") 
if player == 3:
        print("Вы выбрали бумагу.")  
comp = random.randint(1, 3)
if comp == 1:
        print("Компьютер выбрал камень.") 
if comp == 2:
        print("Компьютер выбрал ножницы.")
if comp == 3:
        print("Компьютер выбрал бумагу.")
# определяем победителя
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2 
if player == 2 and comp == 1:
        win = 2  
if player == 2 and comp == 3:
        win = 1 
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("Победил игрок!")
if win == 2:
        print("Победил компьютер!")'''