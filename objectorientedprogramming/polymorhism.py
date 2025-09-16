"""
Polymorphism

def: more than one form (many forms)

1)method_overloading
    :with in same class same method_name different number of parameters XXXX


2)method_overriding



"""


class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

calculator_instance = Calculator()

calculator_instance.add(10,20,30,40)


class Operation:

    def add(self,*args):

        print(sum(args))


operation_instance = Operation()

operation_instance.add(10,20)
operation_instance.add(10,20,30)
operation_instance.add(10,20,30,40)

"""
Topic for tomorrow : functions and lambda function

"""


# (*args,**kwargs)


def add_numbers(*args):

    # *args take any number of parameters as tuple

    print(sum(args))



add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40)


"""
features and applications
datatypes
operators
decisionmaking
looping
functions and lambda function , recursion(pending)
collection properties and methods 
    *list
    *tuple
    *dctionary
    *set
Nested collections

String and string methods

File operations

oops
    >class,object
    >constructor(__init__)
    >magic methods (__str__)
    >inheritance(single,multilevel,multiple)
    >polymorphism(method overloading, method overriding)
    >abstraction ABC abc.py 
    >super and self
    >types of methods 
        *)instance methods
        *)class methods
        *)static method

 *args and **kwargs
 decorator functions
 error handling
 modules and packages 5 to 8 sessions 
 css media query
2.5 

 Database (mysql) (max of 3 session)
 Django(1.5 months)
 DRF(10 sessions)
 javascript(10 session)
 react

"""