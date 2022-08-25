# list comprehensions -генераторы списков
# list comprehensions - упрощенный подход созданию списков,который задействует цикл for ,
# а также конструкции if else для определения того, что в итоге окажется добавлено в наш список
# ==============================
# list -> 0 : 200 -> num%2 =0

# ls = []
# for i in range(0,200):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# with list comprehension
# ls = [x for x in range(0,200) if x % 2==0] 
# print(ls)
# ===============================

# list -> 0 : 200  x
# ls = []
# for x in range(0,300):
#    if x % 2 ==0 and x % 3 ==0:
#     ls.append(x)
# print(ls)   

# with list comprehension
# ls =[x for x in range (0,300) if x%2==0 and x%3==0]
# print(ls)
# ===============================
# ls = []
# for x in range(0,100):
#     if x % 2 == 0:
#         ls.append(x**2)
#     else:
#         ls.append(x)
# print(ls)

# # way list comprehension
# ls =[x**2 if x % 2==0 else x for x in range(0,100) ]
# print(ls)
# ===============================

# синтаксис list comprahension
# newlist  =[expression for item in iterable <if condition == True>]

# ls =[]
# for i in range(0,100,2):
#     ls.append(i)
# print(ls)


# ls =[i for i in range(0,100,2)]
# print(ls)

# ls = [i**2 for i in range(0,11)]
# print(ls)
# =================================
# # @@@@@@@ capitalize in list comprehension
# fruits =['apple','banana','kiwi','mango','limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)
# =================================

# fruits =['apple','banana','kiwi','mango','limon']
# ls =[x.upper() for x in fruits if x != 'apple']
# print(ls)
# +++++++++++++++++++++++++++++++++

# ls = [[1,2,3],[4,5,6],[7,8,9]]
# # result = [1,2,3,4,5,6,7,8,9]]:
# ls1 = []
# for x in ls:
#     ls1 = ls1 + x 
# print(ls1)

# # ++++++++++++++++++++++++++++++++
# ls = [[1,2,3],[4,5,6],[7,8,9]]
# result = []
# for x in ls:
#     result +=[*x]
# print(result)    
# ++++++++++++++++++++++++++++++++++
# ls = [[1,2,3],[4,5,6],[7,8,9]]
# result =[x for inner in  ls for x in inner ]
# print(result)
# =================================

# from datetime import datetime
# finish =[x for x in range(0,100_000_000)]
# ls =[]
# start = datetime.now()
# for x in range(0,100_000_000):
#     ls.append(x)
# finish = datetime.now()
# print(finish-start)    

# ==================================
# ls = [x + 10 if x == 8 else x +100 for x in range(0,10)]
# print(ls)
# ==================================

# dict = {
#     'key1':'value1',
#     'key2':'value2'
# }

# dict_ = {x: x**2 for x in range(1,15)}
# # print(dict_)

# dict1 ={
#     'a':1, 'b':2,'c':3,'d':4,
#     'e':5, 'f':6,'g':7,'h':8
# }
# new_dict ={k: ('even' if v % 2 ==0 else 'odd') for k,v in dict1.items()}
# # #############for k,v in dict1.items():
# print(new_dict)


# names = ['John','Tirion','Jamie','Sansa','Harry']
# dict_names ={i+1: value for i,value in enumerate(names)}
# print(dict_names)


# a = [1,2,3,4,5]
# b =[]

# for i,v in enumerate(a):
#     b.append(i)
#     b.append(v)
# print(b)    

# names = ["Kutman","Sanzhar","Aiana","Janat","Emil"]
# list_ = ['a','e','o','i','y','u']
# # filtered_names=[name for name in names if name[0].lower in list_]
# # print(filtered_names)



# for name in names:
#     if name[0].lower in list_:
#         print(name)
# def countVowels(string):
#    vowels = ['a','e','i','o','u']
#    total = 0
#    for s in string:
#       if s in vowels:
#          total += 1
#    return total



# list_ =list(range(1,11))
# set_ = {num**2 if num % 2==0 else num *3 for num in list_}

# print(set_)






"""
1) Создайте список имён. Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв. Используйте list comprehension.
"""
# names = ["Kutman", "Sanzhar", "Aiana", "Janat", "Emil", "Aliya"]
# # list_ = 'aeiouy'
# list_ = ['a', 'e', 'o', 'i', 'y', 'u']
# f_names = [name for name in names if name[0].lower() in list_]
# print(f'Фильтрованный список имён -- > {f_names}')
"""
2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
Например: 
a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
Результат:
{'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}
"""

# a = {
#     'Sam': {
#         'math': 95,
#         'literature': 88
#     },
#     'Alice': {
#         'math': 70,
#         'literature': 98
#     }
# }

# b = {
#     key: {res: val2 + 2
#           for res, val2 in val.items()}
#     for key, val in a.items()
# }
# print(b)
"""
3) Создайте список чисел от 1 до 10. Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка, в противном случае поместите в список утроенные значения чисел.
"""
# list_ = list(range(1, 11))
# set_ = {num**2 if num % 2 == 0 else num * 3 for num in list_}
# print(set_)
"""
4) Нужно принять строку от пользователя (латиницей) и посчитать в ней количество гласных символов используя list comprehension.
Например:
    input : goremyka
    output : 4
"""
# ls = list(input('Введите строку(латиницей) :'))
# # a = 'aeiouy'
# a = ['a', 'e', 'i', 'o', 'u', 'y']
# list_ = [i for i in ls if i.lower() in a]
# print(f'Kоличество гласных букв: {len(list_)}')


# str = input('Введите строку :')
# t = 0
# for x in str:
#     if x.lower() in 'aeiouy':
#         t = t + 1
# print(f'Количество гласных :{t} ')  


A = ['a','o','e','u','i','y']
Inp = str(input())
Res = [i for i in Inp if i.lower() in A] 
print(len(Res)) 