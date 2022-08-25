'''
tuples() - кортеж ,не изменяемый тип данных

# '''
# thistuple = ('apple','banana','cherry')
# print(thistuple)
# print(type(thistuple))

# mytuple = ('apple') # это стринг
# print(type(mytuple))

# mytuple = ('apple',) # это tuple(потому что стоит запятая)
# print(type(mytuple))

# a = [ 1,2,3,4,5,6]
# b = (1,2,3,4,5,6)
# print('List: ',a.__sizeof__())

# print('Tuple : ', b.__sizeof__())

# tuple_ = tuple('Hello kutman')
# print(tuple_)

# a = 1
# b = 2
# c = 3
# res = (a,b,c)
# print('Res :', res)

# new1,new2,new3 = res
# print(new1)
# print(new2)
# print(new3)

# неизменяемый 
# tuple_ = (1,2,3,4,5)
# del tuple_[0]

# print(dir(tuple))

# tuple_ = (1,2,3)
# res = tuple_.index(3)
# print(res)

# tuple_ = (1,2,3,3,2,1,1,24,2,2)
# print(tuple_.count(2))
'''цикл for'''
# tuple_ = ('apple','banana','cherry')
# for x in tuple_:
#     print(x)

# i = 0 
# while i < len(tuple_):
#     print(tuple_[i])
#     i+=1

# + ,*
# a = (1,2,3)
# b= (4,5,6)
# print(a+b)

# print(a*3)

# tuple_ = ('APPLE','BANANA','CHERRY',1,2,3)
# list_ = list(tuple_)
# list_[0] = "kiwi"
# tuple_ = tuple(list_)
# print(tuple_)

# a = (1,2,3)
# b = list(a)
# b.append(4)
# a = tuple(b)
# print(a)

# c = (5,)
# a +=c  # a = a + c
# print(a)

# # 1)
# tuple_ = (1,8,3,4,5,8,8,9,2)
# target = 8
# # result = (8,3,4,5,8)

# # 2)
# tuple_=(1,2,3,8,5,1,2)
# target = 8
# result = (8,5,1,2)

tuple_ = (1,8,3,4,5,8,8,9,2)
target = 8
begin_index = 0
end_index = -1
if target in tuple_:
    first = tuple_.index(target)

second = tuple_.index(target,first+1)+1
result= tuple_[first:second]  
print(first, second) 
print(result)  


# tuple_ =(1,2,3,8,5,1,2)
# target = 8
# begin_index = 0
# end_index = -1
# if tuple_.count(target) > 1:
#     first = tuple_.index(target)
#     second = tuple_.index(target, first +1)+1
#     result = tuple_[first:second]
# else :
#     first = tuple_.index(target)
#     result = tuple_[first:]

# print(result)

'''
students = (
   ('Елена', '13', 7.1, 'Москва'),
   ('Ольга', '11', 7.9, 'Иваново'),
   ('Елизавета', '14', 9.1, 'Тверь'),
   ('Дмитрий', '12', 5.2, 'Челябинск'),
   ('Максим', '15', 6.1, 'Самара'),
   ('Николай', '11', 8.7, 'Владивосток'),
   ('Артур', '13', 5.8, 'Екатеринбург'),
   ('Jone','13',10, 'WinterFell')

)
total_mark = 0
for student in students:
    # print(students)
    total_mark += student[2]

avg_mark = round(total_mark / len(students),2)
# print(avg_mark)   

good_students =[]
for student in students:
    if student[2] > avg_mark:
        good_students.append(student[0])

# print(good_students)
print(f'Ученики {", ".join(good_students)} в этом семестре хорошо учатся!')

'''