

class Shape:

    def __init__(self,name,edge_count):


        self.name = name

        self.edge_count = edge_count

    def calculate_area(self):

        print(f"calculating{self.name} area")        


class Square(Shape):

    def __init__(self,name,edge_count,s):

        super().__init__(name,edge_count)

        self.s = s

    def calculate_area(self):
        
        a=self.s**2

        print(f"area of {self.name} is {a}")



class Recatngle(Shape):

    def __init__(self, name, edge_count,b,h):
        super().__init__(name, edge_count)
        
        self.b = b

        self.h = h

    def calculate_area(self):
        
        a=self.b * self.h

        print(f"area of {self.name} is {a}")







square_instance1=Square("SQUARE",4,8)

square_instance1.calculate_area()
    

    




class Parent:


    def properties(self):

        print("10kg gold 2car 10lac ")

    
    def marriege_with(self):

        print("marriege with gopalan")

class Child(Parent):

    def marriege_with(self):
        
        print("marriege with DQ")

