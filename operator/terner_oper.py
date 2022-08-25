# 1)
# sentence  = input('Vvedite predlojenie :')

# # if sentence[-1] == '?':
# #     print('Voprositel\'noe predlojeniie!')
# # else:
#     print('Нормальное предложение !')

# 2)  
#    
# # sentence  = input('Vvedite predlojenie :')   
# vopros = '  Вопросительное предложение!'
# normal = 'Нормальное !'
# print( vopros if sentence[-1] == "?" else normal)

'''----------------------------------------------------'''
# Ternary operator - это конструкция, которая аналогична по своему действию конструкции if/else ,но при жтом записывается в одну строчку.

# <выражение если True> if <условие утверждение> else <выражение если False>
# from string import digits
# number = input ('Введите число :')

# for x in number:
#      if x not in digits +'-':
#         raise Exception('Вы ввели не число!')
# number = int(number)

# result = number if number >= 0 else -number
# print(result)        


# a = ["1","2","3"]
# a = map(int, a)
# print(a)
old_list = ['1', '2', '3', '4', '5', '6', '7'] 
new_list = list(map(int, old_list)) 
print(new_list)