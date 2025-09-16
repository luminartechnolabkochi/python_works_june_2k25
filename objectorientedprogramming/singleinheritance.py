
# Single inheritance
# one child class acquiring methods and attributes from one parent class

class Parent:

    def car(self):

        print("parent Swift car")

    def bike(self):

        print("parent passion pro")


class Child (Parent):

    def bike(self):

        print("child triumph bike")

    
child_instance = Child()

child_instance.bike()

child_instance.car()





