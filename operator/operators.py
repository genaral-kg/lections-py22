# операторы стравнения
# < , > , == (равно), <= , >=, != (не равно)

# num1 =18
# num2= 15
# print(18 > 15)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(stroka1<stroka2)
# print(ord('h'))
# print(ord('w'))

# text = 'Hello world'
# for letter in text:
#     print(ord(letter))
# узнать аски коды

# print(chr(1080))



'''Условные операторы
if - если
elif - если иначе
else - иначе
'''
# if <condition>:
#     <body if>
#     <body if>   #срабатывает если в if придет true

# elif<condition>:

# else:
#     <body> # сработает если во всех условиях пришло False
# string = input('Ведите что то :')
# if string == "Hello":
#     print(('Hello stranger!'))
# elif string == 'John':
#     print('Welcome back John Snow!') 
# elif string == 'Mercedez':
#     print("Mercedez-Benz") 
# else :
#     print('Совпадений не найдено')          
# print('Код выполнился!')    

# email = input ('Enter email :')
# password1 = input('Enter password:')
# password2 = input('Enter password confirmation :')

# if len(password1) < 8:
#     raise Exception('Too short password!')
# elif password1 != password2:
#     raise Exeption('Password didn\'t match!')
# else:
#     print('Successfully signed Up!'

''' ----'''
# age = input('Enter your age :')

# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError('Enter correct values!')    
# if age < 18:
#     print(f'chuvak prihodi cherez {18-age} let!!!!')
# else :
#     print("вы проходите по возрасту!")    

'''
password = input('Enter your password: ')
symbols = ['_', ',', '.', '%', '#', '@', '+', '-', '*', '(', ')']

flag = False
for element in symbols:
    if element in password:
        flag = True

if password.isalpha():
    raise Exception('Вы ввели только буквы, нужны еще цифры!')
elif password.isdigit():
    raise Exception('Вы ввели только цифры, нужны еще буквы!')
elif not flag:
    raise Exception('Вы не ввели хотя-бы один спец-символ в пароль!!(_,.()*...)')
else:
    print('Все окей вы ввели корректный пароль!')  '''


# import random
# ver = 0
# while (ver == 0):
#         player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
#         if (player == 1 or player == 2 or player == 3):
#             ver = 1    



# ======================================================================================
# dano [1--100]
# \3 -> 3 - fu
# \5 -> 5 - ba
# \3, \5 -> 15 - fuba

# for number in range(1,100):
#     # print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"{number} - fuba")
#     elif number % 5 == 0:
#         print(f"{number} - ba")
#     elif number % 3 == 0:
#         print(f"{number} - fu")


# num = 1

# while num >= 0:
#     num = int(input('Vvedite chislo :'))
#     if num <= 0:
#         print('Встретилась отрицательное число')

# import random
# ls = ['Plov','Manty','Kuurdak','Lagman','Pelmeni']
# pl = 0
# m = 0
# k = 0
# l = 0
# pe = 0

# for x in range (0,100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         pl +=1
#     elif choice.lower() =='manty':
#         m = m +1
#     elif choice.lower() =='kuurdak':
#         k +=1
#     elif choice.lower() == 'lagman':
#         l+=1
#     elif choice.lower() == 'pelmeni':
#         pe +=1

# print(f'Plow :{pl},Manty :{m},Kuurdak :{k},Lagman :{l},Pelmeni :{pe}')   
# # найти макс потом