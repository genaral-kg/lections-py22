# def cencor(file):
#     with open('forbidden_words.txt') as forbidden_file, open(file) as censor_file:
#         pattern = forbidden_file.read().split()
#         # print(pattern)
#         text = censor_file.read()
#         # print(text)
#         text_lower =text.lower()
#         for word in pattern:
#            text_lower = text_lower.replace(word,'*' * len(word) )
#         print()
#         # print(text_lower)

#         # print(list(zip(text_lower,text)))

#         result = ''.join([y,x][x == '*']for x,y in zip(text_lower,text))

#         print(result)


#         # result = ''
#         # i = 0
#         # for x in text_lower:
#         #     if x == '*':
#         #         result += x 
#         #     else:
#         #         result += text[i]
#         #         i+= 1

#         # print()
#         # print(result)


# cencor('input.txt')


# ===============

# Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:

# количество букв латинского алфавита;
# число слов;
# число строк.

# INUT file.txt:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# OUTPUT
# 108 letters
# 20 words
# 4 lines

# file = open('file.txt')
# letters = 0
# words = 0
# lines = 0
# string = str(file)
# print(file)
# for i in string:
#     if i.isalpha():
#         letters += 1
# print(letters)
# # str = tuple(file)
# file.close()    





# string = '"fddfs456"'

# d = {'Спец.символы': 0, 'Буквы': 0, 'Цифры': 0}
# for i in string:
#     if i.isalpha():
#         d['Буквы'] += 1
#     elif i.isdigit():
#         d['Цифры'] += 1
#     else:
#         d['Спец.символы'] += 1

# print(d['Цифры'], d['Буквы'], d['Спец.символы'])

# with open('file.txt')as file:
#     letters = 0
#     word = 0
    
#     for x in file:
#         res = len((x.split()))
#         word = word + res
#         for i in x:
        
#               if i.isalpha():
#                 letters +=1
       
# file = open('file.txt', 'r')   
# a = (1 for l in file)

    
# print(f'letters {letters}\nword {word}\nlines {a}')
#         #  ref = [row.rstrip() for row in referers]
    
# with open('numbers.txt','w+')as file:
#   number = [num for num in range(1,21)]
#   num = str(number)
#   print(num)
#   file.write(num)
#   for x in file:
#     print(x)
#   with open('squares.txt','w+')as file2:
#     sqares = [sq**2 for sq in number]
#     sqares = [sq**2 for sq in file]
#     print(sqares)
# with open('usernames.txt','w+')as file:
#   while True:
#     name = input("Input your name :")
#     ln = len(name)
#     if name.lower() == "end":
#         break  
#     else:
#         file.write(f"{name} - {ln}\n")
    
# with open('numbers.txt','w+')as file: 
#     for number in range(1, 21): 
#         file.write(f'{number}\n') 
#     file.seek(0) # возвращает курсор в начало 
#     with  open('squares.txt','w+')as file2: 
#         list_of_str = file.readlines() # создает список, 
#         # элементами которого явл каждая строка файла 
#         # print(list_of_str) 
#         list_of_nums = [int(i.replace('\n', '')) for i in list_of_str] # заменяет в каждом элементе \n на пустоту 
#         # затем делает из стринга в интеджер 
#         print(list_of_nums) 
#         for i in list_of_nums:  
#             file2.write(f'{i**2}\n') # записывает каждый элемент листа 
#             # и возводит в квадрат добавляя \n




# with open('numbers.txt','w+')as file: 
#     for number in range(1, 21): 
#         file.write(f'  {number}\n') 
#     file.seek(0)
#     print(list(file))
#     with  open('squares.txt','w+')as file2: 
#         list_of_str = file.readlines() 
#         print(list_of_str) 
#         list_of_nums = [int(i.replace('\n', '')) for i in list_of_str] 
#         # print(list_of_nums) 
#         for i in list_of_nums:  
#             file2.write(f'{i**2}\n') 


# with open('usernames.txt','w+')as file:
#   while True:
#     name = input("Input your name :")
#     if name.lower() == "end":
#         break  
#     else:
#         file.write(f"{name} - {len(name)}\n")

# with open('numbers.txt','w+')as file:
#   number = [num for num in range(1,21)]
#   file.write(str(number))
#   with open('squares.txt','w+')as file2:
#     sqares = [sq**2 for sq in number]
#     print(sqares)
#     file2.write(str(sqares))

# with open('numbers.txt','w+')as file: 
#     for number in range(1, 21): 
#         file.write(f'{number}\n') 
#     file.seek(0) # возвращает курсор в начало 
#     with  open('squares.txt','w+')as file2: 
#         list_of_str = file.readlines() # создает список, 
#         # элементами которого явл каждая строка файла 
#         # print(list_of_str) 
#         list_of_nums = [int(i.replace('\n', '')) for i in list_of_str] # заменяет в каждом элементе \n на пустоту 
#         # затем делает из стринга в интеджер 
#         print(list_of_nums) 
#         for i in list_of_nums:  
#             file2.write(f'{i**2}\n') # записывает каждый элемент листа 
#             # и возводит в квадрат добавляя \n


"""
5)Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.

Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.

Ввод должен быть:
  python_obj = None  
  #ваш остальной код 
  print(json_obj) 

Вывод:
  null 
"""

"""
6)В task2.json хранятся данные в формате JSON.

Напишите программу Python которая будет считывать данные с файла и сохранять их в переменной json_obj.

Затем, преобразуйте это обьект в объект Python и запишите результат в переменную python_obj.
"""
#писать код здесь


"""
1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
# """
# with open('text.txt','r') as file:

#   total = 0
#   sym = 0
#   slow = 0
#   for x in file:

#     for i in x:
#       if i.isalpha():
#         sym += 1
#   print(f'symbols ->{sym}')
#   print(x)

with open('text.txt') as file:
    letters = 0
    word = 0

    for x in file:
        res = len((x.split()))
        word = word + res
        for i in x:

            if i.isalpha():
                letters += 1

file = open('text.txt', 'r')
a = sum(1 for l in file)

print(f'letters {letters}\nword {word}\nlines {a}')
"""
2) Откройте файл task3.txt в режиме записи. Запишите в него числа от 0 до 9 через символ *. Затем вернитесь в начало файла и распечатайте записанные числа. Вывод должен быть:
0*1*2*3*4*5*6*7*8*9
"""
# with open('task3.txt','w+') as f:
#   ls = []
#   for x in range(0,10):
#     ls.append(f'{x}*')
#   f.write(str(ls))
#   f.seek(0)
#   print(ls)
"""
3)Откройте файл task2.txt. В нём записаны числа от 1 до 5 в столбец. Распечатайте все числа, не используя методы.

Вывод в терминале должен быть:
1
2
3
4
5
"""
# file = open('task2.txt')
# a = file.readlines()
# f = [int(f.replace('\n',''))for f in a]
# for x in f:
#   print(x)
# # print(file.read())
# file.close()
"""
4)Откройте файл task5.txt. В нём записаны целые числа. Прочтите эти числа, затем найдите максимальное затем минимальное число. Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)
В файле task6.txt должна быть такая запись: 1-456 
"""
# file1 = open('task5.txt')
# numbers = [int(line) for line in file1]

# file2 = open('task6.txt', 'w')
# file2.write(f"{min(numbers)}-{max(numbers)}")

# file1.close()
# file2.close()
"""
5)Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.

Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.

Ввод должен быть:
  python_obj = None  
  #ваш остальной код 
  print(json_obj) 

Вывод:
  null 
"""
import json

python_obj = None
json_obj = json.dumps(python_obj)
print(json_obj)
"""
6)В task2.json хранятся данные в формате JSON.

Напишите программу Python которая будет считывать данные с файла и сохранять их в переменной json_obj.

Затем, преобразуйте это обьект в объект Python и запишите результат в переменную python_obj.
"""
import json

file = open('task2.json')
json_obj = file.read()
python_obj = json.loads(json_obj)
file.close()
