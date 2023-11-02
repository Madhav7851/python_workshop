class Dog:
    def __init__(self,name):
        self.name=name

dog1=Dog("suraj")
print(dog1.name)


class car:
    def __init__(self,make,mode):
        self.make=make
        self.mode=mode
car1=car("toyota","supra")
car2=car("mercedes","G63")
car3=car("nissan","GTR")
print(car1.mode,car1.make)
print(car2.mode,car2.make)
print(car3.mode,car3.make)

