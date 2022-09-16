import json


def main():
    print('1)Создать объект\n2)Посмотреть базу данных\n3)Посмотреть конкретный объект\n4)Изменить объект\n5)Удалить объект\n6)Поставить лайк машине\n7)Оставить комент машине\n8)Закончить работу ')    
    try:
        a=int(input('Выберите действие:'))
        if a == 1:
            brand=input('Марка:')
            model=input('Модель:')
            year=int(input('Год выпуска:'))
            volume=input('Объём двигателя:')
            color=input('Цвет:')
            body=int(input('Тип кузова:\n1-Седан\n2-Универсал\n3-Купе\n4-Хэтчбек\n5-Минивен\n6-Внедорожник\n7-Пикап\n'))
            if body==1:
                body='Седан'
            elif body==2:
                body='Универсал'
            elif body==3:
                body='Купе'
            elif body==4:
                body='Хэтчбек'
            elif body==5:
                body='Минивен'
            elif body==6:
                body='Внедорожник'
            elif body==7:
                body='Пикап'
            mileage=int(input('Пробег:'))
            price=int(input('Цена:'))
            Cars().create(brand, model, year, volume,color, body, mileage, price)
            main()
        elif a == 2 :
            print(Cars.listing())
            main()
        elif a == 3:
            object=int(input('Введите индекс объекта:'))
            print(Cars.retrieve(object))
            main()
        elif a == 4:
            object=int(input('Введите индекс объекта:'))
            kwargs={}
            obj=input('Что вы хотите изменить?:') #Введите ключ Например: Марка
            val=input('На какое значение вы хотите это изменить?:')#Введите значение Например:'Мерседес'
            kwargs[obj]=val
            Cars().update_car(object, **kwargs)
            main()
        elif a == 5 :
            object=int(input('Введите индекс объекта:'))
            Cars().delete_car(object)
            main()

        elif a == 6:
            id = int(input('Введи индекс объекта:'))
            Cars().like_(id)
            main()
        elif a == 7:
            id=int(input('Введи индекс объекта:'))
            kwargs = {}
            com = input('Коммент: ')
            kwargs['coment'] = com
            Cars().coments(id, **kwargs)
            main()

        elif a == 8:
            print('Работа завершена!!!')
    except:
        print('!!!!!!!НЕКОРЕКТНЫЕ ДАННЫЕ!!!!!!!!')
        main()


class Cars:
    FILE='jsondb/auto.json'
    id=0
    coment=None
    like=0

    def create(self, brand, model, year, volume,color, body,
mileage, price):
        self.brand=brand
        self.model=model
        self.year=year
        self.volume=volume
        self.color=color
        self.body=body
        self.milage=mileage
        self.price=price
        self.send_cars_to_json()
    
    @classmethod
    def get_id(cls):
        cls.id+=1
        return cls.id     
    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    @staticmethod
    def get_one_car(auto,id):
        car= list(filter(lambda x : x['id']==id , auto))
        if not car:
            print('Нет такого продукта ')
        return car[0]


    @classmethod
    def send_auto_to_json(cls, auto):
        with open(Cars.FILE, 'w') as file:
            json.dump(auto, file)

    def send_cars_to_json(self):
        auto=Cars.listing()
        car={
            'id':Cars.get_id(),
            'Марка':self.brand,
            'Модель':self.model,
            'Год выпуска':self.year,
            'Объём двигателя':self.volume,
            'Цвет':self.color,
            'Тип кузова':self.body,
            'Пробег':self.milage,
            'Цена':self.price,

        }
        auto.append(car)
         
        with open(Cars.FILE, 'w') as file:
            json.dump(auto, file)

        return{'satus':'201', 'msg':'car'}

    @classmethod
    def retrieve(cls,id):
        auto = cls.listing()
        car=cls.get_one_car(auto, id)
        return car


    @classmethod
    def update_car(cls,id, **kwargs):
        data=cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_auto_to_json(data)
        print({'status':'200','msg':'Updated'})
    @classmethod
    def delete_car(cls,id):
        data=cls.listing()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car
        index=data.index(car)
        data.pop(index)
        cls.send_auto_to_json(data)
        print({'status':'204','msg':'Deleted'})
    @classmethod
    def like_(cls, id):
        data = cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 1)
        cls.send_auto_to_json(data)
        print({'status':'200','msg':'Liked'})

    @classmethod
    def dislike(cls, id):
        data = cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 0)
        cls.send_auto_to_json(data)
        print({'status':'200','msg':'Disliked'})

    @classmethod
    def coments(cls,id, **kwargs ):
        data=cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_auto_to_json(data)
        print({'status':'200','msg':'Comented'})

with open (Cars.FILE, 'w')as file :
    json.dump([],file)

main()
