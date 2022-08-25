import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

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
        'year of release':int(input('Введите год выпуска :')),
        'price': float(input('Введите цену продукта : ')),
        'description': input('Описание продукта : '),
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    
    result = {'Создан продукт-->': product}
    return result
    
def list_of_products():
    data = get_data()
    for product in data:
        print('Id продукта:', product['id'])
        print('Марка :', product['marka'])
        print('Модель :', product['model'])
        print('Год выпуска :', product['year_of_release'])
        print('Цена :', product['price'])
        print('Характеристика :', product['description'])
        print()

def retrieve_product():
    data = get_data()
    id_product = int(input('Enter Id:'))
    try:
        product = list(filter(lambda x: x['id'] == id_product, data))[0]
    except IndexError:
        print('Such product is None')
    else:
        print('Id продукта:', product['id'])
        print('Марка :', product['marka'])
        print('Модель :', product['model'])
        print('Год выпуска :', product['year_of_release'])
        print('Цена :', product['price'])
        print('Характеристика :', product['description'])
        print()
    
def update_product():
    data = get_data
    id_product = int(input('Enter Id product:'))
    flag = False
    try:
        product = list(filter(lambda x: x['id']== id_product, data))[0]
        print(product)
    except IndexError:
        print('Such product is None')
    else:
        print("b")
        index = data.index(product[0])
        choice = input('Что изменить\'?\n1 - Марка\n2 - Модель\n3 - Год выпуска\n4 - Цену\n5 - Описание:\t ')
        if choice == '1':
            data[index]['marka'] = input('Введите новое название : ')
            flag = True
        elif choice == '2':
            data[index]['model'] = input('Введите модель продукта : ')
            flag = True
        elif choice  == '3':
            data[index]['year of release'] = int(input('Год выпуска : '))
            flag =True
        elif choice == '4':
            data[index]['price'] = float(input('Введите новую цену : '))
            flag = True
        elif choice == '5':
            data[index]['description'] = input('Новое описание продукта : ')
            flag = True
        else:
            print('Такого поля нет!')
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        print('Sucsessfuly updated!')
    else:
        print('Not updated!!!')

def delete_product():
    data = get_data()
    id = int(input('Vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))

    if not product: 
        return {'Сообщение :': 'Неверный id!Продукт не существует!'}

    index = data.index(product[0])
    deleted = data.pop(index)
    
    json.dump(data, open(FILE_PATH, 'w'))
    
    return {'Удален продукт-->': deleted}             