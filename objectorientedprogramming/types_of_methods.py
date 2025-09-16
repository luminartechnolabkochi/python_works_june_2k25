"""
methods are type of functions defined inside class 
there are types of methods 
    1)instance method
    2)class method
    3)static method
"""



class Employee:



    def __init__(self,id,name):

        self.id = id

        self.name = name


    def display_employee(self): #instance method

        print(self.id,self.name)

    @classmethod
    def cls_method_demo(cls):#class method

        print("inside class method")

    @staticmethod
    def satic_method_demo():#static method

        print("inside static method")
    

Employee.cls_method_demo()

Employee.satic_method_demo()






