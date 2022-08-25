#   типы данных  int()
# a = 10
# b = 5
# result = a + b
# print(result)
# print(result+100)

# a = 10
# b = 60
# c = 100
# d = 1000000
# e = 50
# print(a + b + c + d + e)

# / and //
#  5 / 2 = 2.5 -> float
#  5 // 2 = 2 -> целочисленное деление

# num1 = 25
# num2 = 12
# print(num1 / num2)
# print(num1 // num2)

# % -> деление при котором мы получим остаток
# a = 5
# b = 2
# result = a % b
# print(result)

#  ** -> возведение в степень
#  5 ** 4 = 625 
#  5 ** 2 = 5 * 5 = 25
# print(2 ** 4)

# a = 5
# b = 3
# print(pow(a, b))
# print(pow(5, 2, 12))

# round() - округление числа с плавающей точкой

# a = 5.723232
# result = round(a, 3)
# print(result)

# abs() - абсолютное знаечение -> abs(-5) -> 5\
# |-5| = 5

# a = abs (-16)
# print(a)

# divmod(a, b) -> выводит два числа
# первое число это результат целочисленного деление(//) a на b
# второе число это модульное деление(%) а на b 

# result = divmod (5, 2)
# print(result)

# import math 
# a = 25
# print(math.sqrt(a))

# chislo_pi = math.pi
# print(chislo_pi)

# множественное присваивание
# оператор присваивание (=)

# a,  b, c = 1, 2, 7
# print(a, b, c)
# print(a)
# print(b)v
# print(c)

# a, b, c = c, a, b
# print(a, b, c)
# from math import pi
# r = int(input('Vvedite radius :'))
# result_P =  2 * pi * r  
# result_S = pi *(r ** 2)
# print ('Площадь окружности'  , round(result_S,3))
# print ('Периметр окружности' , round(result_P,3))

# a = int(input('Den rojdenia : '))
# b = int(input('Mesyac rojdenia : '))
# c = int(input('god rojdenia : '))
# d = a + b + c
# print(d)

# a = int(input( ' dnyuha : '))

# a = int(input('День рождения : '))
# b = int(input('Месяц рождения : '))
# c = int(input('Год рождения : '))
# d = a + b + c
# print ('Вывод :' ,d)

# a = 600
# b = int(input('vvedite skidku:'))
# c = (a * b) / 100
# d = a - c
# print('Вы должны оплатить ', d, '$')





# name = input("Как тебя зовут?")
# print("Привет ,", name)

# python program.py arg1 arg2


# a = int(input('cifra'))
# b = 3
# c = a * b
# print(c)

# a = int(input("zaebal"))
# print(a)

# a = 600
# b = int(input("skoko skidku hochech?"))
# c = (a / 100) * b
# d = a - c
# print(d, "$")


# from math import pi
# r = int(input("Vesti chislo"))
# S = pi * (r  2)
# l = 2 * pi * r
# print('dlina' , round(l) , 2)
# print('ploshad', round(S) , 2)


# round() - округление числа с плавающей точкой
# a = 5.723232
# result = round(a)
# print(result)

# from math import pi
# r = float(input("Vesti chislo"))
# S = round(pi * (r  2),2)
# l = round((2 * pi * r),2)
# print('dlina' , (l))
# print('ploshad', (S))


# meciac_v_god = 12
# dni_v_god = 365
# meciac_v_7god = 7 * 12
# dni_v_7let = 7 * 365
# print(meciac_v_7god)
# print(dni_v_7let)
# # print(dni_v_7let, meciac_v_7god)

# vysota = 513
# etaj1 = 2.7
# scolco_etaj = vysota / etaj1
# print(scolco_etaj)

# km_bis_mov = 3738
# m_km = 1000
# m_bis_mov = m_km * km_bis_mov
# print(m_bis_mov)

# muka_ton = 255
# gramm = 255 * 1000000
# kg = 255 * 1000
# cent = 255 * 10
# print(cent, kg, gramm)

# z = 2400
# m = 15
# v = m * z
# print(v, '$')
# dol_som = 84
# z_som = dol_som * v
# print(z_som, 'som')

# a = abs(-9)
# print(a)

# a = 4
# b = 8
# c = a  8
# d = b  4
# print (c, d)

# from math import pi
# r = 10
# l = round ((2 * r * pi), 5)
# s = round ((pi * r  2), 5)
# print (l , s)
# S = π × r  2
# pi×(r**2)

# l2 = 5
# l1 = 9
# l = l1 + l2
# s = (l2 + l1) * 2
# print (l, s)

# > Mister:
# a = 4
# b = 4
# c = 4
# d = 4
# s = a  2
# p = a + b + c + d
# print(p, s)

# num = 6
# num = 'box'
# print(num)
# print(type(num))

# str1 = 'Hello world '
# num = 5
# print(num * str1)

# num = 5
# str1 = 'John Snow '
# print(str1 + str(num))

# var = input()
# print(var)
# print(type(var))

# num1 = int(input("vvedite chislo"))
# num2 = int(input('Vvedite stepen '))
# print(num1 , num2)
# print(pow(num1, num2))

# import random

# from random import randint

# name = input ('vvedite imya : ' )
# l_name =input ('vvedite family :')
# num =str(random.randint(10000 , 999999))
# # print(num)
# num = set(num)
# # print(num)

# num = ''.join(num)
# # print(result) 
# result = name + l_name + str(num)
# print(result)

# a = 1
# b = a 
# print(id(a))
# print(id(b))

# print(id(90))