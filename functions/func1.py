# def name_of_function(<a,b> #параметры):
    # <body> #код.которая вовращает конечный результат
    # <return>#оператор для ворвращения результат
# name_of_function(5,6 #аргументы)

# параметры функции -перемнные которые будет принимать наша функция,
# для того чтобы мы могли работать с данными короые передаются в нашу функцию

# Аргументы - это данные которые мы передаем для параметров при вызове функции

# return - оператор для того чтобы функция возврашала результат,
# если return не указать то функция возвращает None(ничего)
# a =print("Hello")
# print(a)

# a=max(range(1,100))
# print(a)

# def our_len(a): #параметр
#     i=0
#     for x in a:
#         i+=1
#     return i  

# ls=[1,2,3,4,5]
# str1="Hello world John Snow"
# print(our_len(ls))    #аргумент


# def sumTwoNums(num1,num2): #параметры
#     result =num1+num2
#     print(result)

# sumTwoNums(5,15)  #аргументс

# def isEven(num):
#     if num %2 == 0:
#         return True
#     print("hello")
#     return False
# print(isEven(6))        


# a= 10
# b =int(input('vveditwe chislo'))


# print(isEven(7))
# print(isEven(a))
# print(isEven(b))


# def isEven1(num:int) ->bool:
#     '''Our function returns True orFalse while checking number for even number'''
#     if num % 2 == 0:
#         return True
#     return False
# print(isEven1(8))        

'''from typing import List
def get_polindrom(words: List[str]) -> List [str]:
    """Function return a polndrom string list"""
    result = []
    for x in words:
        if x.lower() == x[::-1].lower():
            result.append(x)
        return result

some_words = ['John', 'Ono', 'Kazak', 'anna', 'Dovod', 'apa', 'Juice', 'peter', 'piko', 'tenet']
print(get_polindrom(some_words))
print(get_polindrom['John', 'Ono', 'Kazak', 'anna', 'Dovod', 'apa', 'Juice', 'peter', 'piko', 'tenet'])

здесь ощибка есть исправить надо
'''

def substract():
    num1 = 20
    num2 = 5