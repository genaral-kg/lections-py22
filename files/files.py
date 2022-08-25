# Работа с файлами
# каретка - указатель - курсор

# open(<путь до вашего файла>)

# file = open('/home/kutman/desctop/py.22/files/files.py') #абсолютный путь 
 
# file = open('files.py') #относительный путь

# print(file)

# режимы работы с файлами 
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)

# file = open('text.txt','r')
# print(file)
# data = file.read()
# print(data)
# data = data.split('\n')
# print(data)
# print(type(data))

# data = file.readline()
# print(data)
# # hello world
# # 
# data1 = file.readline()
# print(data1)
# # my name is John Snow
# 
# data = file.readlines()
# print(data)
# ###['hello world\n', 'my name is John Snow\n', "I'm 23 years old\n"]

# data = file.readlines()[1]
# print(data)


# file = open('text.txt','w')
# print(file)
# file.write('Hello world!\nMy name is John Snow!')
# file.close()



# file = open('text.txt','w+')
# print(file)
# file.write('Hello world!\nMy name is John Snow!wewr')
# print(file.tell())
# file.seek(0)
# print(file.tell)
# print(file.read)
# file.close()


# #контекстный менеджер 
# with open('text.txt','r')as file:
#     data = file.read()
#     print(data)
# ##print(file.read())



# ls = ['Hello World','My name is Kutman','I\'m 35 years old']
# with open('text.txt','w')as f:
#     f.writelines(line + '\n' for line in ls)


# info = {'kutman','mederbekov','21 years old'}
# with open('text.txt','w') as f:
#     f.writelines(line +'\t' for line in info)




# ------------------------------------------
# работа с фотографиями

# from PIL import Image
# import pytesseract
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s.\d+',string))
#         print('!!!')
#         print(list_of_imei)
#     with open('imeicodes.txt','w') as file:
#         for x in list_of_imei: 
#             for i in x:
#                 file.write(f'{i}\n')

# ls = ['imei.jpeg','/home/hello/desktop/py.22/files/imei.jpeg']
# get_imei_codes(ls)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


