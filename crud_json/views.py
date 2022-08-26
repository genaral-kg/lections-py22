import json
FILE_PATH = 'data.json'


def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def list_of_products():
    data = get_data()
    for product in data:
        print('Id продукта:', product['id'])
        print('Марка :', product['marka'])
        print('Модель :', product['model'])
        print('Год выпуска :', product['year_of_release'])
        print('Цена :', product['price'])
        print('Характеристика :', product['description'])
    return''
    
def retrieve_product():
    data = get_data()
    id_product = int(input('Введите id продукта:'))
    try:
        product = list(filter(lambda x: x['id'] == id_product, data))[0]
    except IndexError:
        print('Неверный id!Продукт не существует!')
    else:
        print('\nId продукта:', product['id'])
        print('Марка :', product['marka'])
        print('Модель :', product['model'])
        print('Год выпуска :', product['year_of_release'])
        print('Цена :', product['price'])
        print('Характеристика :', product['description'])
    return ''
def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt','w')as file:
        file.write(str(id))
        return id

def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'marka': input('Введите марку продукта : '),
        'model':input('Введите модель продукта :'),
        'year_of_release':int(input('Введите год выпуска :')),
        'price': round(float(input('Введите цену продукта : ')),2),
        'description': input('Описание продукта : '),
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)    
    result = {'Создан продукт-->': product}
    return result

def update_product():
    data = get_data()
    flag = False
    id = int(input('Введите id продукта : '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product:
        return 'Неверный id!Продукт не существует!'

    print(product)
    index = data.index(product[0])
    choice = input('Что изменить?\n1 - Марка\n2 - Модель\n3 - Год выпуска\n4 - Цену\n5 - Описание\t ')
    if choice == '1':
        data[index]['marka'] = input('Введите новое название : ')
        flag = True
    elif choice == '2':
        data[index]['model'] = input('Введите модель продукта : ')
        flag = True
    elif choice == '3':
        data[index]['year_of_release'] = int(input('Год выпуска : '))
        flag =True
    elif choice == '4':
        data[index]['price'] = round(float(input('Введите новую цену : ')),2)
        flag = True
    elif choice == '5':
        data[index]['description'] = input('Новое описание продукта : ')
        flag = True
    else:
        print('Такого поля нет!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

    if flag:
        return {'Обновлен продукт-->':data[index]}
    else:
        return 'Не обновлено!'

def delete_product():
    data = get_data()
    id = int(input('Введите id продукта : '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product: 
        return 'Неверный id!Продукт не существует!'

    index = data.index(product[0])
    deleted = data.pop(index)
    
    json.dump(data, open(FILE_PATH, 'w'))
    
    return {'Удален продукт-->': deleted}
