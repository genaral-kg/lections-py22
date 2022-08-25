'''
while <expression>:
    <body>
'''
# i = 1
# while i <=10:
    # print(f'Цикл выполнился {i},раз!')
    # i += 1

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' or name2.lower() !='raychel':
#     name1 = input('vvedite imya1: ')
#     name2 = input('vvedite imya2: ')
#     i += 1
#     if i > 5:
#         print('Цикл отсановлен!')
#         break
# else:
#     print('Vy vveli pravilnoe imya!')    

# admin = ['John','ilovepython123']
# i = 3
# password = None

# while admin[1] != password:
#     password = input(f'{admin[0]} enter password : ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 dney1')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zawli v sistemu!')    

# for <variable>  in <iterable object>:
    # <body>

list_ = [0,1,2,3,4,5,6,7,8,9]

# i = iter(list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))

# for i in list_[::-1]:
    # print(i) 

# secret_list = ['DeltaViskey','LOTR123','WhiteHorse']
# nick = input('VVEDITE SVOI NICK :')
# while nick not in secret_list:
#     print('Incorrect nick ,try one more time :')
#     nick = input('VVEDITE SVOI NICK :')
# else:
#     print(f'You\'re welcome my dear friend,{nick}!')    

# 6 = 6,3,2,1
# num =2
# for i in range (0,23436):

# n = 23436
# i = 1
# a = []
# while i ** 2 <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# a.sort()
# print(a)


import random
ls = []
for x in random(1,100):
    ls.append(random.randint(1,15))

print(sorted(ls))
res = list(set(ls))
print(res)    