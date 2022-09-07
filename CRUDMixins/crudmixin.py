from search import search_object

class CRUDMixin:
    def _get_or_set_object_and_ID(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def create(self, **kwargs):
        self._get_or_set_object_and_ID()
        self.id += 1 
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}

    def list(self): 
        result = []
        for obj in self.objects:
            result.append({'id': obj['id'], 'title': obj['title'], 'price': obj['price']})
        return {'status': 200, 'msg': result}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}
    @search_object    
    def update(self,id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}
    @search_object
    def delete(self,id,**kwargs):
        obj = kwargs['object_']
        if obj:
            self.objects.remove(obj)
            return{'status':204,'msg':'Succesfullyvdeleted!'}
        return {"status":404,"msg":"Not Found!"}

    def save(self):
        import json
        with open('data.json','w')as file:
            json.dump(self.objects,file)
        
        return "SAVED!"

            

smartphones = CRUDMixin()
print(smartphones.create(title='Redmi Note 10', description='The best for own price!', qty=10, price=200))
print(smartphones.create(title='Redmi Note 20', description='Flagman of redmi phones, Best!', qty=3, price=500))
print(smartphones.create(title='Iphone 14 Pro Max', description='New phone for ponts!', qty=5, price=1300))
# print(smartphones.list())
# print(smartphones.detail(1))
print()
# print(smartphones.update(2,title = "Iphone 11",qty = 10))
print()
# print(smartphones.detail(2))
print(smartphones.delete(2))
print()
print(smartphones.list())

print(smartphones.create(title='Samsung 22', description='The best android smartphone!', qty=10, price=200))
print(smartphones.create(title='Nokia 1110', description='good telephone!', qty=3, price=500))
print(smartphones.save())