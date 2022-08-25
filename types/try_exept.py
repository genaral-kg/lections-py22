# Обработка исключений
# Operator: Try...except

# Ошибки -> связанные с кодом:
# Syntax Error
# IndentationError
#    if a > 0
    # print(a)
# TypeError
# Исключение -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# ValueError
# ImportError
# BaseException #Прородитель всех ошибок

# Try...except
# try:
#     <exprssion>
# except <Exception>:
#     <bode>
# <else>: Если всё ок
#     <body>
# <finally>: В любом случае сработает в конце.
#     <body>

# print(dir(builtins))

# num1 = int(input('Введите число: '))
# print(num1)
# print('Ochen\' vajnaia strochka koda! ')


# try:
#     num1 = int(input('Введите число: '))
#     print(num1)
# except:
#     print('Invalid Value, try again!')

# print

# print('Ochen\' vajnaia strochka koda! ')

# Способы увидеть ошибку
# 1. import sys

# ls = [1, 2, 3, 4, 5,]

# try:
#     index = int(input('Vvedite oshibku index: '))
#     print(ls[index])
# except:
#     import sys
#     print(f'oops, we catched {sys.exe_info() [0]} error! ')

# 2. Exception as e 

# while True:
#     try:
#         index = int(input('Vvedite oshibku index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'oops, we catched {e.class} error! ')

#+=+=+=+=+=+=+=+=+=+=+=+=++=+=+=+=+=+=+=+=+=+
# try:
#     num1 = int(input("Введите число!: "))
#     num2 = int(input("Введите число 2: "))
#     res = num1 / num2
# except ValueError:
#     print('Вы ввели некорректные данные! ')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')

# else:
#     print("Result of division", res)
# finally:
#     print('The end ')


"""
1) Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 лет, Эржану - 21 лет, Чынгызу - 24 лет, Алтынай - 17 лет, Асеме - 16 лет.
Напишите программу которая определяет кого пустить в ночной клуб а кого нет. (работа со словарем)
"""




"""
2) Задание 7
В блоке try запросите у пользователя ввод его возраста. Затем в том же блоке проверьте его возраст на совершеннолетие.
 Если пользователь несовершеннолетний(младше 18), выбросите исключение ValueError с текстом: Доступ запрещён
Обработайте это исключение и другое исключение, которое возникает при вводе текста вместо возраста, выдав сообщение: 
Введён некорректный возраст
Если ошибок не возникло распечатайте сообщение: Спасибо
и, наконец, распечатайте сообщение: До свидания!
вне зависимости от того, произошла ошибка или нет.
"""
# try:
#     age = int(input('Enter your age: '))
#     if age < 18:
#         raise Exception('Доступ запрещен!')
# except ValueError:
#     print('Введен некоректный возраст!')
# else:
#     print('Спасибо')
# finally:
#     print("До свидания!")    


"""
3) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
"""
# a = {"banana":3,"apple":5,"mango":8}

# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)

# print(a)
"""
4) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
"""
# a = {"a":1,"b":2,"c":7}
# total = 0
# for v in a.values():
#   total += v
# print(total)
"""
5) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
"""
# my_dict = dict()
# for i in range(1, 11):
#     my_dict[i] = pow((i),2)

# print(my_dict)



"""
6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями.
 Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
"""
  
    
"""
7) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет.
"""




"""
8) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
"""

# try:
#     a = int(input('Enter : '))
#     if a <= 0:
#         raise Exception('Do not enter negative intergers or zero')
# except ValueError:
#     print('Enter integer, not string')
# else:
#     print(f'сумма : {a}')   


from random import random
ls = []
def add():
    print('ADD!')
    name = input('Vvedite imya: ')
    ls.append(name)

def remove():
    print('REMOVE!')
    if not ls:
        print('Увы в списке имён пусто')
        return
        
    index = input('Vvedite index: ')
    l = [1,2,3,4,5]
    try:
        print(ls.pop(index))
    except IndexError:
        print('Нет такого индекса!')
    except ValueError:
        print('Вы ввели некоректный индекс!')

for x in range(0,10):
    func = print(random.choice([add,remove]))
    func()