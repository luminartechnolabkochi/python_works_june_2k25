

class Animal:

    def sound(self):

        print("animal sound method")

# IS A 

class Cat(Animal):

    def sound(self):
        super().sound()
        print("cat sound meow")



cat_instance = Cat()

cat_instance.sound()

