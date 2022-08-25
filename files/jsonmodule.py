# JavaScriot Object Notation - JSON
# Единный формат ъхранения и передачи данных между копьютерами,сервисами,приложениями
# и языками програмированея через сеть Интернет
# <filename>.json
# {
#     "id":1,
#     "author":"John",
#     "posts":Null

# } ---Это JSON, ЗАДАЧА НАУЧИТСЯ ПЕРЕВОДИТЬ JSON в Python Dict

# !!!
# JS object = {},PY dict == {}, JSON == {}

# преоцессы Сериализации и Десериализации данных
"""
Сераилизация (запись данных  в JSON)- это перевод Pthon Dict в Json формат

dump - метод записывает объект python в файл в формате Json

dumps - метод записывает объект pyhton в строку в формате JSON

Десериализация(Чтение данных из JSON)- жто процесс перевода из JSON в python dict

load - метод которвый считывает файл в формате JSON и переводит его в обхект Python

loads - метод который считывает текст в формате JSON и переводит его в объекты Python
"""

"""============================================================="""
# Десериализация

# import json
# from urllib.request import urlopen
# data = urlopen('https://randomuser.me/api/')
# # print(type(data))
# # print(data)
# py_dict = json.load(data)
# print(py_dict)
# print(type(py_dict))

# import json

# with open('downAPI.json','r') as file:
#     data = file.read()

#     # print(data)
#     # print(type(data))
#     user = json.loads(data)
#     print(user)
#     print(type(user))

"""======================================"""
# Процесс сериализации ---dump---
import json

dict_= {
    'name':'John',
    'l_name':'Snow',
    'status':True,
    'wife':False,
    'child':None,
}
# string = json.dumps(dict_)
# print(string)
# print(type(string))

with open('new.json','w')as file:
    json.dump(dict_,file)