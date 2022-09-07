
def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for object_ in self.objects:
            if object_.get('id') == id:
                kwargs.update(object_=object_)
                return func(*args, **kwargs)
        
    return wrapper