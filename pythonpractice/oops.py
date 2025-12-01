"""class Car:
    def __init__(self, brand=None):   # brand made optional
        self.__brand = brand          # private variable

    def set_brand(self, brand):
        self.__brand = brand          # setter

    def get_brand(self):
        return self.__brand           # getter

    def accelerate(self):             # fixed spelling
        print("Car is accelerating...")

def main():
    c1 = Car()                        # object created
    c1.set_brand("BMW")               # using setter
    print("Brand:", c1.get_brand())   # using getter
    c1.accelerate()                   # calling method

if __name__ == "__main__":
    main()"""
#from abc import ABC, abstractmethod

"""class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    def race(self):
        print("pallavi")

class BMW(Car):
    def start(self):
        print("BMW car starts with a push button")

# c1 = Car() 

c2 = BMW()
c2.race()
c2.start()"""
class parent:
    def __init__(self,brand):
        self.brand=brand
class child(parent):
       def __init__(self,brand):
           self().__init__(brand)
       def plan(self):
            print("good")
c1=child()
c1.plan()
print(cl.brand("pallavi"))
