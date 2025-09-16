
"""
Method overriding 

* customize behaviour in child class without changing parent class

* To provide specific implimentation of a method that is already defined in parent class 

"""

class Parent:

    def home(self):

        print("parent home method")

    def vehicle(self):

        print("parent passion-pro vehicle")

class Child(Parent):

    def vehicle(self):

        print("child duke method")

    


child_instance = Child()

child_instance.home()

child_instance.vehicle()




