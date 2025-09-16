

class Student:    
    school_name = "ABC"    
    def __init__(self,rol,name,total):
        
        self.rol = rol

        self.name = name

        self.total = total

    @classmethod
    def update_school_name(cls,new_school_name):

        cls.school_name = new_school_name

        print(cls.school_name)

    @staticmethod
    def is_pass(total):

        return True if total>140 else False
    
student_instance1= Student(1000,"hari",145)

student_instance2= Student(1002,"vipin",135)

Student.update_school_name("CMS")

print(Student.is_pass(student_instance1.total))


print(Student.is_pass(student_instance2.total))



# OOPS END 


#@abstractmethod
#@classmethod
#@staticmethod



        