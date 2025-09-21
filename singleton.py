class Singleton:
    _instance=None
    def __new__(cls):
        if(cls._instance is None):
            cls._instance=super().__new__(cls)
        return cls._instance
    #using cls._instance this mean for each sub class will take a new instance , but if 
    #we use Singleton._instance that mean one instance over all classes(even of sub class)
 
obj1=Singleton()
obj2=Singleton()
print(obj1==obj2)
print(obj1 is obj2)    