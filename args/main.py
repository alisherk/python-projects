# default arguments
from email.mime import multipart


def add1(a, b=5):
    print(a, b)

# add(2, b=10)

#unlimited arguments *args 

def add2(*args): 
    # print(type(args))  typeof tuple
    # print('position', args[0])
    for n in args: 
        print(n)

# add2(2, 3, 6)

#keyword arguments **kwargs produces a dict of key value pairs
def calculate(**kwargs):
    print(kwargs) # {'add': 3, 'multiply': 5}
    for key, val in kwargs.items(): # we cal also access values like this print(kwargs["add"])
        print(key, val)

def calculate2(n, **kwargs): 
   n += kwargs["add"]
   n *= kwargs["multiply"]
   print(n)

calculate2(2, add=3, multiply=5)

class Car: 
     def __init__(self, **kw) -> None:
         self.make = kw.get("make")  #get will allow avoid class init problem
         self.model = kw.get("model")

car = Car(make="Nissan")

print(car.make)
