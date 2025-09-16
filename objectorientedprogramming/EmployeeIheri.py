

class Employee:

    def __init__(self,name,salary):

        self.salary = salary

        self.name = name

    def calculate_salary(self):

        print(self.salary)


class Manager(Employee):

    def __init__(self, name, salary):

        super().__init__(name,salary)        

    def calculate_salary(self):
        self.salary+=5000

        print(self.salary)


class Developer(Employee):

    def __init__(self, name, salary):
        
        super().__init__(name,salary)

    def calculate_salary(self):
        
        self.salary+=2500

        print(self.salary)




manager_instance1 = Manager("vijay",23000)

developer_instance1 = Developer("ram",20000)

manager_instance1.calculate_salary()