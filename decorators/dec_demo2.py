

def abs_dec(fun):

    def wrapper(num1,num2):

        return fun(abs(num1),abs(num2))
    
    return wrapper

@abs_dec
def add_number(num1,num2):

    return num1+num2


print(add_number(-10,10))

# builtin decorators
# @abstractmethod
# @classmethod
# @staticmethod
# @property


class Employee:

    def __init__(self,id,name,department):

        self.id = id

        self.name = name

        self.department = department

    @property
    def get_name(self):

        print(self.name)

employee_instance = Employee(120,"vijay","hr")

employee_instance.get_name

print(employee_instance.id)

print(employee_instance.department)



