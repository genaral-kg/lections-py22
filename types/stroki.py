"hello world"
's vami Kutman'

'''
hello worldell
'''

"""
hello
"""

# a = 5  
 '''Строки в Pythone - набор последовательных символов , которые мы используем для хранени и представления текстовой информации'''

# индексация в строке

# name  =  'John'
#     # j = 0 = -4
#     # o = 1 = -3
#     # h = 2 = -2
#     # n = 3 = -1
       
# print(name)
# print(name[1])       
# print(name[-1])

# str1 = 'birthday'
# # print(str1[5],str1[6],str1[7])

# # срезы по индексам
# # [start: end: <step>]
# print(str1[5:8])
# print[str1[5:]]

# print(str1[0:5])
# print(str1[:5])

# text = 'Hello world! My name is Jonh! I\'m King of North! '
# print(text)
# print(text[:13])
# print(text[::2])
# print(text[::-1])

# # конкетенация строк
# a = 'hello'
# b= 'world'
# c= " "
# res = a + c + b
# print(res)

''' Экранирование - при помощи которого можно выставлять символы в строку,которые сложно ввести с клавиатуры.
\n ->  перенос строки
\t - горизонтальная табуляция
\v ->вертикальная табуляция
\f ->перевод страницы
\r -> возврат указателя
'''

# name = 'Jonh\nSnow'
# print(name)
# print(len(name))
# name = 'Jonh\tSnow'
# print(name)
# name = 'Jone\vSnow'
# print(name)
# name = 'Jone\fSnow'
# print(name)
# name = 'Jone\rSnow'
# print(name)

'''
Форматирование строк
1 с помощью %
2 с использованием .format()
3 интерполяция строк (f - строки)
'''
# %
# name = input (' Enter your name :')
# last_name = input ('Enter your last name :')
# print('Hello mr/mrs %s %s'%(name,last_name))

# .format
# name = input (' Enter your name :')
# last_name = input ('Enter your last name :')
# print('Hello mr/mrs{} {}'.format(name,last_name))

# f- сторки 
# a = input ('enter mr/mrs :')
# name = input('Enter your name :')
# l_name = input('Enter your last name :')
# print(f'Hello {a} {l_name} {name}.Welcome to the parthy!')

'''print(dir(str))'''