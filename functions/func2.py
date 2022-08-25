"""def get_some_data(a,b,*args,**kwargs):
    print('параметры a и b:',a,b)
    print('Аргументы :',args)
    print('Именованные аргументы :',kwargs)
    print(args[0])
    print(args[-1])
    print(kwargs['name'])

get_some_data(1,2,3,4,5,lang='Python',name='John Snow',car='BMW M8')
"""

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
def generate_random_string(len_):
    import string as s
    import random
    random_str = ''.join(random.choice(s.ascii_lowercase+s.ascii_uppercase+s.digits) for i in range(0,len_))

    return random_str
print(generate_random_string(15))
"""
# -=-=-=-=-=-=--=-=-=-=--=-=-=--=-=-=
''
"""
def add(a,b):return a+b

def subtract(a,b): return a-b

def multiply(a,b): return a*b

def divide(a,b): 
    try:
        return a/b
    except ZeroDivisionError:
        return'На ноль делить нельзя!'

def main():
    try:
        num1 = float(input('Введите первое число :'))
        num2 =float(input('Введите второе число :'))
    except ValueError:
        print('Вы ввели некоректное число!')
        
    operator = input('Введите оператор(+,-,/,*):')
    if operator == '+': print(f'result :{add(num1,num2)}')
    elif operator == '-': print(f'result :{subtract(num1,num2)}')
    elif operator == '*': print(f'result :{multiply(num1,num2)}')
    elif operator == '/': print(f'result :{divide(num1,num2)}')
    else:print("Вы ввели неверный оператор!")
    question = input("Хотите продолжить?(Yes/No: ")
    if question.lower() == 'yes':
        main()
    else:
        print("Спасибо за использование нашего калькульятора!Good bye!")

main()
"""
def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

def calc(num1, num2):
    operator = input('Введите оператор(+,-,/,*): ')
    if operator == '+': return add(num1, num2)
    elif operator == '-': return subtract(num1, num2)
    elif operator == '*': return multiply(num1, num2)
    elif operator == '/': return divide(num1, num2)
    else: return 'Вы ввели неверный оператор!'

def main():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели некоректное число!')
        main()
        return

    while True:
        result = calc(num1, num2)
        if type(result) != float:
            print(f'Result: {result}')
        else:
            print(f'Result: {result}')
            break

    question = input('Хотите продолжить?(Yes): ')
    if question.lower() == 'yes':
        main()
    else:
        print('Спасибо за использование нашего калькулятора! Пока!')

main()



