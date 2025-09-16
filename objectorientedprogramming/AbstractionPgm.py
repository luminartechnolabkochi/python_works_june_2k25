"""
Abstraction:

    Hiding implimentation details and showing essential features

    


"""

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Swift(Vehicle):

    def start(self):
    
        print("swift  start ")

swift_instance = Swift()

swift_instance.start()




