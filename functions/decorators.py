"""from random import choice
 
def add():
    global c
    print('ADD!')
    c.append(input('Введите имя '))
    print(c)
    return 1
 
def remove():
    print('REMOVE!')
    global c
    if not len(c): return
    del c[int(input(f'Удалить имя от 0 до {len(c) - 1} '))]
    print(c)
    return 1
 
c = []
i = 0
while i < 10:
    if choice([add, remove])():
        i += 1
print(c)"""

# DECORATORS
# ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА - это функция корорая в качестве аргумента принимает другую функцию4

# Декоратор - это функция которая позволяет без измениение кода 
# обернуть другую функцию для того чтобы расширит функционал обернутой функции

# def decorator(func):
#     print(func)
#     print('Я декоратор!')
#     return func()

# def hello():
#     print('Я hello!')
#     return 'Hello'

# def john():
#     print('Я John')
#     return 'John'

# print(hello())
# print()
# print(decorator(john))
# print()
# print(decorator(hello))


# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции{func.__name__},заняло :{finish - start}')

# def loop():
#     i = 0
#     range_number = 1000000
#     while i <= range_number:
#         print(i)
#         i+=1

# benchmark(loop)

# Pythonic way -> @benchmark
# Синтаксический сахар - крастора кода

# +=+=+=+=+=+=+=+=+=+=++==+=+=+=+=+==++==++=+=+=+=+=+=+=
# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции{func.__name__},заняло :{finish - start}')
#     return wrapper
# @benchmark
# def loop():
#     i = 0
#     range_number = 1000000
#     while i <= range_number:
#         print(i)
#         i+=1

# @benchmark
# def add():
#     i = 0
#     range_number = 1000000
#     ls = []
#     for i in range(0,range_number):
#         ls.append(i)
#     print(ls)

# loop()
# add()

# ++++++++++++++++++++++++++++++++++++++
"""def strong(func):
    def wrapper(*args,**kwargs):
        return '<strong>' + func() +'</strong>'
    return(wrapper)

def div(func):
    def wrapper(*args,**kwargs):
        return'<div>' + func() + '</div>'
    return wrapper
@strong
@div
def get():
    return 'John Snow'

print(get())
"""
# ###  <strong><div>John Snow</div></strong>
# ---------------------------------------
"""def uppercase_decorator(function):
   def wrapper():
       func = function()
       make_uppercase = func.upper()
       return make_uppercase
   return wrapper


# @uppercase_decorator
# def say_hi():
#    return 'hello there'
# print(say_hi())
def split_string(function):
   def wrapper():
       func = function()
       splitted_string = func.split()
       return splitted_string
   return wrapper

@split_string
@uppercase_decorator
def say_hi():
   return 'hello there'
print(say_hi())
"""

# def decorator_with_arguments(function):
#    def wrapper_accepting_arguments(arg1, arg2):
#        print("My arguments are: {0}, {1}".format(arg1,arg2))
#        function(arg1, arg2)
#    return wrapper_accepting_arguments
# @decorator_with_arguments
# def cities(city_one, city_two):
#    print("Cities I love are {0} and {1}".format(city_one, city_two))
# cities("Nairobi", "Accra")

# +++++++++++++++++++++++++++++++++++++++++
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#        print('The positional arguments are', args)
#        print('The keyword arguments are', kwargs)
#        function_to_decorate(*args)
#    return a_wrapper_accepting_arbitrary_arguments
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#    print(a, b, c)
# function_with_arguments(1,2,3)

# @a_decorator_passing_arbitrary_arguments
# def function_with_keyword_arguments():
#    print("This has shown keyword arguments")
# function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

"""def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
   def decorator(func):
       def wrapper(function_arg1, function_arg2, function_arg3) :
           "This is the wrapper function"
           print("The wrapper can access all the variables\n"
                 "\t- from the decorator maker: {0} {1} {2}\n"
                 "\t- from the function call: {3} {4} {5}\n"
                 "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                         function_arg1, function_arg2,function_arg3))
           return func(function_arg1, function_arg2,function_arg3)
       return wrapper
   return decorator
pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
   print("This is the decorated function and it only knows about its arguments: {0}"
          " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))
decorated_function_with_arguments(pandas, "Science", "Tools")"""

# import functools
# def uppercase_decorator(func):
#    @functools.wraps(func)
#    def wrapper():
#        return func().upper()
#    return wrapper
# @uppercase_decorator
# def say_hi():
#    "This will say hi"
#    return 'hello there'
# print(say_hi())


# print(say_hi.__name__)
# #'say_hi'
# print(say_hi.__doc__)

# def check_password(func):
#     def wrapped():
#         return func().strip()
#     return wrapped

# @check_password
# def get_password():
#     a = input('Vvedite password :')
#     return a

# print(get_password())    



# def check_password(func):
#     def wrapped(param):
#         return func(param).strip()
#     return wrapped
# # @check_password
# # def get_password(parametr):
# #     return password

# # password = input('Vvedite password :')
# # print(get_password(password))

# @check_password
# def get_info(param:str) ->str:
#     return info
# info = input('info :')
# print(get_info(info))


# def check_password(func):
#     def wrapper(parametr):
#         return func(parametr).strip()
#     return wrapper

# @check_password
# def get_info(param:str) ->str:
#     return param

# param = input('Vvedite info :')
# print(get_info(param))


# def bread(func):
#     def wrapped(*args):
#         print('</-----\>')
#         func(*args)
#         print('</_____\>')
#     return wrapped

# def ingredients(func):
#     def wrapped(*args):
#         print('#tomat#')
#         func(*args)
#         print('#salad#')
#     return wrapped


# @bread
# @ingredients
# def get_sendwich(*fillers):
#     for filler in fillers:
#         print(filler)

# get_sendwich('--apple--','sousage','^ketchup^')



# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f'see what I got :{args}')
#         print(f'see what I got :{kwargs}')
#         func(*args,**kwargs)
#     return wrapper
# @decorator
# def with_params(name,last_name):
#     print("I'm with parametrs")
#     print(f'Hello {name} {last_name}')

# print(with_params('kutman',last_name = 'Mederbekov'))

# def benchmark(iters:int)->int:
#     def actual_decorator(func):
#         import time
#         def wrapper(*args,**kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.time()
#                 func_call =func(*args,**kwargs)
#                 end = time.time()
#                 total = total + (end - start)
#             print(f'Average complete time:{total / iters}')
#             return func_call
#         return wrapper
#     return actual_decorator

# @benchmark(iters = 10)
# def get_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     # return webpage.text


# print(get_webpage(url = 'http://yandex.ru'))

# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
      
#     return wrapper

# @call_function
# def first():
    
#     print("hello world")
#     return "hello world"
# first()

# print(f"Вызов функции {first.__name__} прошёл успешно")
# ++++++++++++++++++++++

# def func_start_time(func):
#     import datetime
#     def wrapper():
#         dt_now = datetime.datetime.now()
#         print(dt_now)
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()


# from functools import reduce 
# ls = ['kutman', 'emil','makersbootcamp','helloworld']
# max = reduce(lambda a, b : a if (len(a) > len(b)) else b, ls) 
# print(max)

# 111111111111111111111111111
# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
        
      
#     return wrapper

# @call_function
# def first():
#     print("hello world")
#     return 'hello world'

# first()


# 2222222222222222222222222222222222222

# def func_start_time(func):
#     import datetime
#     def wrapper():
#         dt_now = datetime.datetime.now()
#         print(f'Функция запушена',dt_now.strftime("%d-%m-%Y %H:%M"))
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()
# def call_function(func): 
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func() 
#         print(f"Вызов функции {func.__name__} прошёл успешно") 
#     return wrapper
# @call_function 
# def first():
#     print("hello world")
#     return 'hello world' 
# first()
# def make_bold(func):
#     def wrapper(*args,**kwargs):
#         return '<b>' + func() +'</b>'
#     return wrapper

# def make_italic(func):
#     def wrapper(*args,**kwargs):
#         return'<i>' + func() + '</i>'
#     return wrapper

# def make_underline(func):
#     def wrapper(*args,**kwargs):
#         return'<u>' + func() + '</u>'
#     return wrapper
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())

import datetime
def func_start_time(func):
    def wrappers():
        print(f'Функция запущена {datetime.datetime.now()} ')
        func()
    return wrappers
    


@func_start_time
def func():
    print('Hello world')
func()
