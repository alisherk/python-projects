# inheritance 

class Animal: 
    def __init__(self):
        self.num_eyes = 2
   
    def breath(self): 
        print('Inhale, exhale')


class Fish(Animal):
    def __init__(self): #inherit from Animal class
        super().__init__() 

    def breath(self): #overide breath method
        super().breath()
        print('doing this underwater')

    def swim(self): 
        print('moving in water')


nemo = Fish()

nemo.swim()

nemo.breath()