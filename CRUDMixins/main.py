from views import CreateMixin,RetrievMixin,UpdateMixin,DestroyMixin
import json

class Product(CreateMixin,RetrievMixin,UpdateMixin,DestroyMixin):
    def save(self):
        with open("data1.json","w")as file:
            json.dump(self.objects,file)
        return {"msg":"saved!!!"}



class Order:
    discount = 10
    def __init__(self) -> None:
        self.orders = []
        self.product = Product()
        self.product.post(title="Iphone 14 Pro Max",description="The best new phone",qty = 5,price = 1399)
        self.product.post(title="Nokia 1110",description="Old telephone",qty = 10,price = 199)

    def create_order(self,objects):
        ls = []
        for item in objects:
            for product in self.product.objects:
                if item['id'] == product['id']:
                    self.subtract_qty(item,product)
                    ls.append({"title":product['title'],"qty":item["qty"],"price":product["price"]})
        self.orders.append(ls)
        money = self.total_count(ls)
        return {'Order':ls,"Total sum":money}

    def total_count(self,objects):
        total_count = 0
        for product in objects:
            price = product ['price']
            qty = product['qty']
            total_count += self.make_discount(price,self.discount) * qty 
        return total_count

    def subtract_qty(self,item,product):
        result = product['qty'] - item['qty']
        if result < 0:
            raise Exception("Too many qty of product!")
        product['qty'] = result

    def make_discount(self,price,percent):
        return price - (price/100 * percent)

orders = Order()
print("Before:",orders.product.get())
products = [{'id':1,"qty":3,"id":2,"qty":2}]
print(orders.create_order(products))

print("After:",orders.product.get())







# smartphones = Product()
# print(smartphones.post(title="Iphone 14 Pro Max",description="The best new phone",qty = 5,price = 1399))
# print(smartphones.post(title="Nokia 1110",description="Old telephone",qty = 10,price = 199))
# print(smartphones.get())
# print(smartphones.patch(2,title = "Nokia 10 pro maxxxx",qty =4))
# print(smartphones.get_detail(2))
# print(smartphones.delete(2))

# print(smartphones.post(title="Samsung S 22 Ultra",description="The best new phone on androin OC1",qty = 17,price = 1199))
# print(smartphones.save())