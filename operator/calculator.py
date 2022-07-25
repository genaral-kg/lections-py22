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



# 2
import string
flag = True
symbols = string.digits + '-'+ '.'
# print(symbols)
# print(type(symbols))

while flag:
        is_correct_nums = True
        num1 = input("Введите первое число : ")
        for x in num1:
                if x not in symbols:
                    print('Вы ввели некоректное число!') 
                    is_correct_nums = False  
                    break
        if not is_correct_nums:
                continue
        num2 = input("Введите первое число : ")
        for x in num2:
                if x not in symbols:
                    print('Вы ввели некоректное число!') 
                    is_correct_nums = False
                    break
        if not is_correct_nums:
                continue  
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2) 

        operator = input("Введите оператор(+, - , * , /) :") 
        if operator =="+": print( num1 + num2)
        elif operator ==  '- ': print(num1 - num2)
        elif operator == "*" : print( num1 * num2)
        elif operator == "/":
                if num2 == 0:
                        print('Нельзя делить на ноль!')
                else:
                        print( num1 / num2)
        else :
                print('Неправильный оператор !!!') 
        choice = input('Хотите продолжить(yes/no):')
        if choice.lower == " no ":
                flag = False

                