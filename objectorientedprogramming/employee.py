



# Employee (id,name,department,salary)[set_employee(),display_employee()]


class Employee:

    id:int

    name:str

    department:str

    salary:int

    def set_employee(self,id,name,department,salary):

        self.id = id

        self.name = name

        self.department = department

        self.salary = salary

    def display_employee(self):

        print(self.id,self.name,self.department,self.salary)

emp_instance1 = Employee()

emp_instance2 = Employee()

emp_instance1.set_employee(1000,"ram","hr",56000)

emp_instance1.display_employee()