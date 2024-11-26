# use of *args can be used for any number of arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1,2,3))



# use of **kwargs

def cal(n, **kwargs):
    #print(kwargs)
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    #print(n)

cal(2,add=2,multiply =2)

class Car:

    def __init__(self, **kw):
        #self.make = kw["make"]
        #self.model = kw["model"]
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
print(my_car.make)
