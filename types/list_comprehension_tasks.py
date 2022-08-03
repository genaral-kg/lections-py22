"""
1) Создайте список имён. Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв. Используйте list comprehension.
"""
names = ["Kutman", "Sanzhar", "Aiana", "Janat", "Emil", "Aliya"]
# list_ = 'aeiouy'
list_ = ['a', 'e', 'o', 'i', 'y', 'u']
f_names = [name for name in names if name[0].lower() in list_]
print(f'Фильтрованный список имён -- > {f_names}')
"""
2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
Например: 
a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
Результат:
{'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}
"""

a = {
    'Sam': {
        'math': 95,
        'literature': 88
    },
    'Alice': {
        'math': 70,
        'literature': 98
    }
}

b = {
    key: {res: val2 + 2
          for res, val2 in val.items()}
    for key, val in a.items()
}
print(b)
"""
3) Создайте список чисел от 1 до 10. Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка, в противном случае поместите в список утроенные значения чисел.
"""
list_ = list(range(1, 11))
set_ = {num**2 if num % 2 == 0 else num * 3 for num in list_}
print(set_)
"""
4) Нужно принять строку от пользователя (латиницей) и посчитать в ней количество гласных символов используя list comprehension.
Например:
    input : goremyka
    output : 4
"""
ls = list(input('Введите строку(латиницей) :'))
# a = 'aeiouy'
a = ['a', 'e', 'i', 'o', 'u', 'y']
list_ = [i for i in ls if i.lower() in a]
print(f'Kоличество гласных букв: {len(list_)}')

## str = input('Введите строку :')
## t = 0
## for x in str:
##     if x.lower() in 'aeiouy':
##         t = t + 1
## print(f'Количество гласных : {t}')