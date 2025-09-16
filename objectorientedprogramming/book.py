

# Book (name,author,price) initalize attributes

# ClassName => PascalCase

"""
Constructor

def : is a special method that is automatically invoked when an object of the class is created
*used for initailize instance variable
*constructor special_name : __init__

__str__,

human readable string representation of an object

__ magic methods, dunder methods


"""




class Book:

    def __init__(self,name,author,price):

        self.name = name

        self.author = author

        self.price = price

    def display_book(self):

        print(self.name,self.author,self.price)

    def __str__(self):
        
        return self.name

 


book_instance1 = Book("goat life","benyamin",560)

book_instance1.display_book()


print(book_instance1) #Book_object_at_x123456



# 