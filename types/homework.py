# Kutmans homework!
"""
По теме: Типы данных. Числа.
"""
"""
1. Дана переменная с длиной стороны квадрата, найдите периметр и площадь, распечатайте результат в терминале
"""
# a = int(input('введите сторону : '))
# p = a*4  # так как квадрат,
# s = a**2

# print('P = ',p)
# print('S = ',s)


# введите сторону : 5
# P =  20
# S =  25


"""________________________________________________________________________________________________________
 2. Даны переменные со сторонами прямоугольника, найдите периметр и площадь, распечатайте результат в терминале
"""

# import math
# a = int(input("Введите сторону a = "))  
# b = int(input("Введите сторону b = "))  
# c = int(input("Введите сторону c = "))  

# p =(a +b + c) / 2
# s =math.sqrt(p*(p-a)*(p-b)*(p-c))

# print('P = ', p)
# print('s = ', s)

# Введите сторону a = 4
# Введите сторону b = 
# Введите сторону c = 3
# P =  6.5
# s =  5.332682251925386

# _____________________________________________________________________________________________________________

"""
3. Дана переменная с радиусом окружности, найдите периметр и площадь окружности, результат выведите в терминал

"""
# from math import pi
# r = int(input('Введите радиус :'))4
# result_P =  2 * pi * r  
# result_S = pi *(r ** 2)
# print ('Площадь окружности ='  , round(result_S,3))
# print ('Периметр окружности =' , round(result_P,3))

# Введите радиус :5
# Площадь окружности = 78.54
# Периметр окружности = 31.416

# _____________________________________________________________________________________________________________
"""
4. Даны две переменные с четными числами, переумножьте первое число саму на себя столько раз, сколько хранится число во второй переменной,
 вторую переменную переумножьте, соответственно столько раз, сколько хранится в первой переменной, распечатайте результат в терминале
"""
# a = int(input('vvedite chislo :'))
# b = int(input('vvedite 2 chislo :'))
# c = a ** b
# d = b ** a
# print(c)
# print(d)

# vvedite chislo :2
# vvedite 2 chislo :3
# 8
# 9
"""
5. Дана переменная с отрицальным числом, сделайте её позитивным, распечатайте результат
"""
# a = abs (-16)
# print('Положительное = ', a)

# Положительное =  16

# ______________________________________________________________________________________________________________
"""
6. Дана переменная с температурой воздуха по фаренгейту(float), переведите это значение в температуру по Цельсию, и распечатайте результат в терминале
"""
# f = float(input(" Введите температуру в градусах Фаренгейта:  "))
# c = 5 / 9 * (f - 32)
# print('Цельсий = ', c)

#  Введите температуру в градусах Фаренгейта:  100
# Цельсий =  37.77777777777778


"""
7. От Бишкека до Москвы расстояние составляет 3 738 км, вычеслити расстояние от Бишкека до Москвы в метрах, и распечатайте результат в терминале 
"""
# L = 3738
# B_M = L * 1000
# print('растояние от Бишкека до Москвы = ', B_M ,'метр')

# растояние от Бишкека до Москвы =  3738000 метр

 
# _____________________________________________________________________________________________________________________________
"""
8. Дана переменная со целочисленным значением весса муки в 255 тонны, найдите сколько это будет в граммах, килограммах, центнерах, 
распечатайте результат в терминале 
"""
# t = 255
# k = 255 * 1000
# g = k * 1000
# ts = 255 * 10
# print('killogram = ',k)
# print('gram = ', g)
# print('tsentner = ',ts)


# killogram =  255000
# gram =  255000000
# tsentner =  2550

#_______________________________________________________________________________________________________________________________
"""
9. Найдите сколько месяцев и дней пройдёт за 7 лет, распечатайте результат в терминале (в 1 году 365 дней)
"""
# let = 7
# mes = 7 * 12
# den = 7 * 365
# print('месяц = ', mes)
# print('день = ', den)


# месяц =  84
# день =  2555

"""
10. Высота небоскрёба 513 метров, рассчитайте сколько будет этажей в здании, если высота одного этажа планируется в 2.7 метров, результат распечатайте в терминале
"""
# high = 513
# h_etag = 2.7
# etag = int(high / h_etag)
# print('Этажи = ', etag)

# Этажи =  190

# _________________________________________________________________________________________________________________________________
"""
11. Работнику начисляли зарплату в 2400 долларов 15 месяцев, распечатайте сколько заработал за этот период работник, в сомах, курс доллара к сому использовать 84 сома к 1 доллару, результат распечатайте в терминале
"""
# zarplata =  2400
# kurs_dollar =  84
# v_som = zarplata * kurs_dollar
# print ('Он заработал ', v_som ,'сом')

# Он заработал  201600 сом