"""
1) Перейдите в домашнюю папку по абсолютному пути (не используя ~)
"""
# cd 


"""
2) Объявите три переменные с целочисленными значениями x, y, z. Затем обменяйте их значения в одно действие. Переменной x присвойте значение переменной y. Переменной z присвойте значение переменной x. А переменной у присвойте значение переменной z.
"""

# x = 4
# y = 9
# z = 8
# a = (x, y, z) = (z , y , x)
# print(a)


# забыл 


"""
3) Высота небоскрёба 513 метров, рассчитайте сколько этажей в здании, если высота одного этажа 2.7 метров, результат распечатайте в терминале 
"""
# h = 513 
# h_etag = 2.7
# etag = h / h_etag 
# print ('etagi = ',etag)


"""
4) Работнику начисляли зарплату 2400 долларов 15 месяцев, распечатайте сколько заработал за этот период работник, в сомах (курс доллара к сому использовать 84 сома к 1 доллару) результат распечатайте в терминале
"""

# zarplata_v_dollar  =  2400
# kurs_dollar =  84
# v_som = zarplata_v_dollar * kurs_dollar
# print ( v_som)


"""
5) Дана переменная с отрицальным числом, сделайте её позитивным, распечатайте результат
"""
# a = int (input('vvedite chislo : '))
# d = abs(a)
# print(d)
"""
6) Дана переменная с целочисленным значением весса муки в размере 255 тонны, переведите данную массу в граммы, килограммы, центнеры. Распечатайте результат в терминале 
"""
# tonna =  255
# kg = tonna * 1000
# g = kg * 1000
# ts = tonna * 10
# print ('tonna = ', tonna)
# print ('kilogram = ', kg)
# print('gram = ', g )
# print('tsentner = ', ts)
"""
7) Создать целое число y.
Возведите его в квадрат и найдите остаток от деления на 5 и распечатайте результат.
"""
# a = int(input('введите целое число : '))
# b = a ** 2
# c = a % 5
# print('квадрат =' , b)
# print ('остаток от деления = ',c)
"""
8) Создать десятичное число с переменной decimal.
Найдите и распечатайте его квадрат, куб, квадратный корень.
"""
# from math import sqrt

# decimal = float(input('vvedite chislo :'))
# kv = decimal ** 2
# kub = decimal ** 3
# koren = sqrt(decimal)
# print (kv)
# print(kub)
# print(koren)
"""
9) В переменные a, b запишите два числа, которые будут обозначать два катета прямоугольного треугольника .
Рассчитайте длину гипотенузы треугольника c, воспользовавшись теоремой Пифагора.
Note: Теорема Пифагора: квадраты катетов = квадрату гипотенузы.
Распечатайте результат
"""
# from math import sqrt
# a = int(input('vvedite katet :'))
# b = int(input('vvedite 2 katet :'))
# c= sqrt(a ** 2 + b ** 2)
# print(c)

"""
10) Примите от пользователя 3 числа inp1, inp2, inp3 из вкладки INPUT,
Перемножьте первые два числа,
Найдите остаток от деления на третье число.
Распечатайте полученный результат.
"""
# inp1 = int(input('vvedite chislo :'))
# inp2 = int(input('vvedite chislo :'))
# inp3 = int(input('vvedite chislo :'))
# c = inp1 * inp2
# d = c % inp3
# print (c)
# print(d)