
#### Method1 does not allow subclassing ####
class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

        return cls.__instance


#### Method2 allows subclassing ####

class SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwds):
        if cls.__instance is None:
            cls.__instance = super(SingletonMeta, cls).__call__(*args, **kwds)
        
        return cls.__instance
        

class Logger(metaclass=SingletonMeta):
    def log(self, msg):
        print(msg)

#### test it out ###

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)

l1 = Logger()
print(l1)
l2 = Logger()
print(l2)

