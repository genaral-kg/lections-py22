'''Напишите мини-проект “Калькулятор”. Для этого, вам необходимо
вспомнить стандартный ввод и вывод данных, тип данных Числа и операции над
числами. Также вам потребуется помощь условных операторов.
Требования:
1. Ваш калькулятор должен запрашивать последовательно первое число,
затем второе число. Затем калькулятор должен запросить операцию, которую он
произведет с числами (сложение, вычитание, умножение, деление, остаток от
деления, возведение в степень, целочисленное деление)
2. Далее калькулятор выдает вам ответ.
3. Если пользователь вводит несуществующую операцию, калькулятор
выводит сообщение: “Данной операции нет в системе”
Пример:
Ввод:
Введите первое число: 3
Введите второе число: 7
Выберите операцию из следующих +-*/%**// : *
Вывод:
Ответ: 21

Пример:
Ввод:
Введите первое число: 3
Введите второе число: 7
Выберите операцию из следующих +-*/%**// : =
Вывод:
Ответ: Данной операции нет в системе
'''
# KUTMANMEDERBEKOV_CALCULATOR

num =  int(input("Введите первое число: "))
num1 = int(input("Введите второе число: "))
   # num =  float(input("Введите первое число: "))
   # num1 = float(input("Введите второе число: "))

oper = (input("Выберите операцию из следующих + - * / % ** //  :"))
print('Вывод : ')
if oper == '+':
        print("Ответ :",num + num1)
elif oper == '-':
        print("Ответ :",num - num1)       
elif oper == '*':
        print("Ответ :",num * num1) 
elif oper == '/':
        print("Ответ :",num / num1)
elif oper == '%':
        print("Ответ :",num % num1)                  
elif oper == '**':
        print("Ответ :",num ** num1)         
elif oper == '//':
        print("Ответ :",num // num1)         
else:
    print("Данной операции нет в системе!")


# Введите первое число: 125
# Введите второе число: 25
# Выберите операцию из следующих + - * / % ** //  :/
# 5.0

# Введите первое число: 45
# Введите второе число: 6
# Выберите операцию из следующих + - * / % ** //  ://
# 7

# Введите первое число: 5
# Введите второе число: 7
# Выберите операцию из следующих + - * / % ** //  :*
# 35

# Введите первое число: 35 
# Введите второе число: 90
# Выберите операцию из следующих + - * / % ** //  :=
# Данной операции нет в системе!