
"""

*args  is non key word arguments allows you to pass any number of parameters(receives parameters as tuple)
**kwargs (key word arguments) (receives parameters as dictionary)

"""

def add_numbers(*args):

    print(type(args))

    return sum(args)





def display_person_details(*args):

   print(args) #("james","street1","uk","london")

   name=args[0]
   address=args[1]


   print(name)
   print(address)
   native_place=args



display_person_details("james","street1","uk","london",456789)



def display_student_details(**kwrags):#kwargs={"roll":1234,"name":"tom","place":london}

    print(kwrags)


display_student_details(roll=1234,name="tom",place="london")










