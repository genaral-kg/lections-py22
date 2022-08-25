# Область видимости и пространство имен или scopes
# определяет контекст переменной, в рамках которого мы можем ее использовать


# built-in(встроенная) -print,len,max
# global(Глобальная)
# enclosed(не локальная,nonlocal )
# local(локальная)
"""x = 200
def myfunc():
    print(x)
    x =300
    print(x)
myfunc()
print(x)
"""

# a = 10 #global
# print #built-in
# def hello(): #global
#     a = 'hello world' #local
#     print(a, 'local inside at func')

# hello()
# print(a,'global')

# x = 'global'
# print(x,"1")

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x,"3")
#     print(x,"2")
#     local()
#     print(x,"4")

# enclosed()
# print(x,"5")

# LEGB
#   local - enclosed - global - built-in

# len = 5
# len()
# print(len([1,2,3,4,5]))
# ++++

# a =10 
# def func():
#     print(a)
#     a =  15
#     print(len)
# func()


# var =100 #global vaariable
# x  = 5
# def increment():
#     print(x)
#     # var += 1 #try to update a global variable inside local scope
#     # print(var)
#     # x = 10 
# increment()



# global -> позволяет  изменят значение глобальной облсати видимости



# var = 100

# def increment():
#     global var
#     var += 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)



# def counter():
#     num = 0 
#     def increment():
#         nonlocal num
#         num +=1
#         return num
#     return increment
# c = counter()
# print(c) #<function counter.<locals>.incrementer at 0x7f22a88c30d0>
# print(c()) #1
# print(c()) #2
# print(c()) #3
# b = counter()
# print(c()) #1
# print(b())
# print(c())


# i  = 0
# for x in range(0,9999):
#     if x %3 == 0 and x % 5 == 0:
#         i +=1
#         print(x)
# print(i)        


# print(dir(__builtins__))
# print(len(dir(__builtins__)))


# print(abs(-15)) #стандартный вызов встроенной функции
# abs = 10 # переопределяем строенное имя abs 
# # print(abs(-15))
# print(abs)
# del abs
# print(abs(-25))
# print(abs)


# print(globals())
# print(locals())


# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5]] -> 6, 11 -> 11

# list_ = [[1,2,3],[3,3,5],[5,5,5,5] ]
# for x in list_:
#     res = max([sum(x) for x in list_])
# print(res)
# sums = []  
# for x in list_:
    
#     sums.append(sum(x))
#     print(sums)


# ls = [[1,2,3],[3,3,5],[5,5,5,5] ]
# def find_max(ls):
#     sums = []
#     for x in ls:
#         sums.append(sum(x))
#     return max(sums)
# print(find_max(ls))


# res = max([sum(x)for x in ls])
# print(res)



# list_ = [[1,2,3],[3,3,5],[5,5,5,5] ]
# res = max([sum(x) for x in list_])
# print(res)