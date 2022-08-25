''' 
list - (список,массив) - изменяемый, последовательный тип данных ,
который из себя представляет коллекций каких либо объектов(значений).
'''
# my_list = [1, 'string',False,None,[1,2,3]]
# print(my_list)
# print(type(my_list))

# print(my_list[0])
# print(my_list[-1][0])

# my_list = list('Hello world!')
# print(my_list)
# print(len(my_list))

# tuple_ = ('banana','emilbanana','apple')
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))

'''
range() - возвращает последовательность элементов (числа)
 
'''
# ls = list(range(0,100))
# print(ls)


# ls = list(range(0, 101))
# # print(ls)
# for x in ls:
#     # print(x)
#     if x % 2 == 0:
#         print(f'Chislo {x} chetnoe, kvadrat {x**2}')
#     else:
#         print(f'Chislo {x} nechetnoe, kvadrat {x**3}')


# print(dir([]))
# append(element) - Добавляет element в конец списка.
# list_ = [1, 2, 3, 4, 5]
# print(list_)
# list_.append(6)
# list_.append([1,2,3])
# print(list_)

# extend(element[iterable]) -> расширяет список добавляя element в конец.
# ls = [1, 2, 3]
# ls.extend([11, 12, 13])
# ls.append([11, 12, 13, 14])
# print(ls)

# insert(<index>, <element>) -> Добавляет element по указаному индексу.
# ls = ['string', 2, 3, False]
# ls.insert(1, 1)
# ls.insert(-1, None)
# print(ls)

# index(element, [start], [end]) -> возвращает индекс element в списке

# ls = ['Hello', 'world', 'my', 'name', 'is', 'John', 'North', 'king', 'queen', 'USA']
# str1 = input("Введите слово: ")
# if str1 in ls:
#     print(f'"{str1}" is in list: {ls.index(str1)}')
# else:
#     print('Isn\'t')

# print(ls[ls.index('queen')])

# count(element) -> Возвращает кол-во вхождений element в списке.

# ls = [1, 2, 3 ,4 ,5, 6, 7, 8,9 ,5, 5 ,5 ,5 ,5 ,5]
# result = ls.count(5)
# print(result)

# remove(element) -> Удаляет elemen, но если такого элемента нет в списке, то тогда выводится ошибка.
# pop([index]) -> Удаляет и возвращает элемент по индексу, но если индекс не указан, то удаляет последний элемент.

# ls = [1, 2, 3, 4, 5, 6, 7]
# ls.pop()
# print(ls)
# ls.remove(1)
# print(ls)

# ls = [5, 1, 2, 3, 4, 5, 6]
# ls.remove(5)
# print(ls)

# for x in ls:
#     if 5 in ls:
#         ls.remove(5)
# print(ls)

# sort() - сортирует список, если в аргументах передать reverse=True, то список будет отсортирован в убывающем порядке.

# import random
# ls  = []
# for x in range(0,200):
#     ls.append(random.randint(0,1000))
# ls.sort(reverse=True)
# print(ls)
# print(len(ls))



"""
1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
Например: 
Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
Вывод: 5 8
[5, 7, 8, 1, 3, 0, ‘Makers’]
"""
# numbers = input("Введите семь чисел через запятую : ").split(',')
# numbers_int = []
# for i in numbers:
#   numbers_int.append(int(i))

# print(numbers_int[0],numbers_int[-1]) 
# numbers_int.pop()
# numbers_int[-1] = 'Makers'
# print(numbers_int)
"""
2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в отсортированном виде в порядке возрастания.
"""
# from random import sample

# numbers = sample(range(0,20),k = 10)
# print(numbers)
# print(sorted(numbers))

"""
3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
"""

# ----------------========================================================-----------------

# text = "ha ha ha ha"
# # print(text[::-1])
# result = text.replace('a','i',2)
# print(result)

# str1 = 'Hello World! My name is John Snow!'
# print(str1.replace('John','Kutman'))


'''strip () - убирает пробельные символы в начале и в конце строки.'''
# rstrip - убирает пробелы из правой стороны 
# lstrip - убирает пробелы из левой стороны

# text = input('Enter some text :')
# print(text)
# result= text.strip()
# print(result)


# text = '   hello world   '
# print(len(text))
# result= text.strip()
# print(result)
# print(len(result))

'''startswith(string, [ start], [ end] - возвращает True если строка начинается с string ,иначе False'''

# text = 'Hello World'
# print(text.startswith('W'))
# print(text.startswith('H'))
# print(text.startswith('Hello'))
# print(text.startswith('d', -1))
# print(text.startswith('Wo', 6))

# ----------------------------------------------
# print(id('h'))
# print(id('H'))

# ----------------------------------------------

# print(dir(str))

'''
isalpha() - проверяет состоит ли наша строка из символов (букв латинского алфавита или криллицы)

isdigit() - проверяет есть ли в нашей строке числа, если есть хоть одна то выводит True

isalnum() - проверяет состоит ли наша строка полностью из чисел
'''
# text = 'ПРИВЕТ'
# print(text.isalpha())

# text = '45'
# print(text)
# print(text.isalpha())

# K.u.t.m.a.n
'''text = 'Kutman'
result = tuple(text)
dot = '.'.join(result)
print(dot)'''





'''str.istitle
index(value, [start],[end])- выводит индекс значения value в нашей строке
'''

# text = 'Hello world!My name is John!'
# result = text.index('o',15)
# print(result)

# rindex - поиск с конца
# find(value , [start], [end]) - делает тоже самое что и метод index .Разница в том что, если value не найден ,то возвращается -1
# rfind

# text = 'hello'
# print(text.rfind('l'))

# count('string') - считает количество вхождений string в нашу строку

# text = 'Hello World!I\'m from Earth!'
# result = text.count('o')
# print(result)

'''swapcase() - Возвращает строку,в которой каждая буква будет иметь противоположный регистр'''
# upper()
# lower()

# text = 'Hello World, John Snow'
# print(text.swapcase())
# # print(text.lower())
# # print(text.upper())

'''capitalize() - переводит первую букву в верхний регист'''

# print('hello'.capitalize())
# print(input('Vvedite vashe imya :').capitalize().istitle())

# title() - переводит символы всех слов в строке в верхрний регистр
# text = 'john kutman jerry'
# print(text.title())
# print(text.capitalize())

'''split(разделитель) - дробит строку по разделителью который находится в строке.
Разделяет строку и возвращает тип данных list'''



# text = 'Let me speak from my heart in English'
# ls = text.split(' ')
# print(ls)

# # разделитель.join(iterable) - соединяет строки ,которые находится в iterable по разделителью

sentence = '*'.join(ls)
print(sentence)
sentence = ' | '.join(ls)
print(sentence)

word = 'Hello'
res = word[-1] + word[1:-1] + word[0]
print(res)

# word = 'sentence'
# result = f'{word[-1:]}{word[1:-1]}{word[:1]}'
# print(result)


