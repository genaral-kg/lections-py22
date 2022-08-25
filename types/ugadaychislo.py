'''
 ТЗ “Угадай число”

Напишите мини-проект “Угадай число”. Для этого, вам
понадобиться стандартный ввод/вывод данных, тип данных числа
и условные операторы. Также не забудьте использовать
библиотеку random.
Требования:

1. Ваша программа должна запрашивать имя пользователя.
Программа должна запросить у пользователя хочет ли он играть
или нет. Если ответ будет ‘нет’, то программа должна
завершиться.

2. Далее пользователь должен угадать число. Также вы должны
сделать счетчик попыток, и показать пользователю сколько
попыток ему потребовалось, чтобы отгадать число.

3. Если пользователь угадал число, запросить у него хочет ли он
пройти игру еще раз, если ответ будет “нет”, программа должна
завершиться
'''
"""KUTMAN'S CODE"""
'''
from random import randint
while True:

    name = input('Введи свое имя :\n')
    
    play = input("Хочешь ли ты играть? (y/n): ") 
    
    if play.lower() != "y": 
        break 

    number = randint(1, 20)
    print (f'Отлично, {name}, я загадал число между 1 и 20. Сможешь угадать?')

    guesses_made = 0
    while guesses_made < 4:
   
        guess = int(input('Введи число: '))

        guesses_made += 1

        if guess < number:
            print ('Твое число меньше того, что я загадал.')

        if guess > number:
            print ('Твое число больше загаданного мной.')

        if guess == number:
            break

    if guess == number:
        print (f'Ух ты, {name}! Ты угадал мое число, использовав {guesses_made} попыток!')
    else:
        print (f'А вот и не угадал! Я загадал число {number}')

    
    play_again = input("Сыграем еще? (y/n): ") 
    if play_again.lower() != "y": 
        break 

'''
   
# Введи свое имя :
# Aiana
# Хочешь ли ты играть? (y/n): y
# Отлично, Aiana, я загадал число между 1 и 20. Сможешь угадать?
# Введи число: 10
# Твое число меньше того, что я загадал.
# Введи число: 15
# Твое число меньше того, что я загадал.
# Введи число: 18
# Ух ты, Aiana! Ты угадал мое число, использовав 3 попыток!
# Сыграем еще? (y/n): y
# Введи свое имя :
# Sanzhar
# Хочешь ли ты играть? (y/n): y
# Отлично, Sanzhar, я загадал число между 1 и 20. Сможешь угадать?
# Введи число: 9
# Твое число меньше того, что я загадал.
# Введи число: 8
# Твое число меньше того, что я загадал.
# Введи число: 7
# Твое число меньше того, что я загадал.
# Введи число: 6
# Твое число меньше того, что я загадал.
# А вот и не угадал! Я загадал число 15
# Сыграем еще? (y/n): n 





# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# _____________________________________________________________________________________

# ДРУГОЙ ВАРИАНТ №2
'''
import random

input('Введите имя')
select = input('Хотите поиграть? (да/нет):')

i = 0
while i == 0:
    if select == 'да' or select == 'Да':
        num = random.randint(0, 10)
        # print(num)
        j = 0
        count = 0
        while j == 0:
            user_num = input('Введите число от 0 до 10:')
            if user_num.isdigit():
                user_num = int(user_num)
                if num == user_num:
                    select = input(f'Вам потребовалось {count + 1} попыток \nХотите поиграть еще раз? (да/нет):')
                    j = 1
                elif num != user_num:
                    count += 1
            
    elif select == 'нет':
        print('Программа закрыта')
        i = 1
    else:
        print('Введите именно да или нет:')
        select = input('Хотите поиграть? (да/нет):')
'''

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# ПРОСТЫЕ ЗАДАЧИ 



# a = 1
# while a <= 10:
  
#     print(a**2)
#     a += 1

    #возвести 2 в степен от 0 до 20 
# p = 0
# while p < 20:
#     p += 1   
#     print(2 ** p)

# вывести только строчные буквы
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# clean_string = ''
# for letter in letters:
#     if not letter.isupper():
#         clean_string += letter
# letters = clean_string
# print(letters)




# rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# for i in range(11):
#     print('^' * 27)
#     for letter in rus_lower:
#         if rus_lower.index(letter) % 11 == i:
#             print('| ', letter.upper(), letter, ' |', end='')
#     print()
# print('^' * 27)
# # Результат:
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  А а  ||  К к  ||  Х х  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Б б  ||  Л л  ||  Ц ц  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  В в  ||  М м  ||  Ч ч  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Г г  ||  Н н  ||  Ш ш  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Д д  ||  О о  ||  Щ щ  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Е е  ||  П п  ||  Ъ ъ  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Ё ё  ||  Р р  ||  Ы ы  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Ж ж  ||  С с  ||  Ь ь  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  З з  ||  Т т  ||  Э э  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  И и  ||  У у  ||  Ю ю  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# |  Й й  ||  Ф ф  ||  Я я  |
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^





# 1111
# list_ = ['Kutman','Sanzhar','Aiana','Sultan','Janat']

# for i in list_:
#     print(i)

# 2222
# list_ = [1,2,3,4,5,6,7,9,12,13,15]
# list1 =[]
# list2 =[]
# for num in list_:
#     if num % 2 == 0:
#         list1.append(int(num))
#     else:
#         list2.append(int(num))
# print('Четные --->',list1)
# print('Нечетные --->',list2)        



# 3333
# from random import sample

# numbers1 = sample(range(0,10),k = 5)
# numbers2 = sample(range(0,10),k = 5)
# print('numbers 1 ---> ',numbers1)
# print('numbers 2 ---> ',numbers2)
# numbers = numbers1 +numbers2
# print('numbers ---> ',numbers)
# print(sum(numbers))

# 4444
# year = 2019

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('ВИСОКОСНЫЙ ГОД')
# else:
#     print('Невисокосный год')


# list_ = [1,2,3,4,5]

# for item in list_:
#     fact = 1
#     for number in range(1, item+1):
#         fact = fact * number
#     print ("{}! = {}".format(item, fact))


    