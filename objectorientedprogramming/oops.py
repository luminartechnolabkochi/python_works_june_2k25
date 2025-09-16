# ObjectOriented programming

# class  [attributes,methods]
# object
# self 


# Animal name,sound  set_animal(name,sound)

class Animal:

    name:str

    sound:str

    def __init__(self,name,sound):

        self.name = name

        self.sound = sound

    def animal_sound(self):

        print(self.name,"===",self.sound)

    def __str__(self):
        return self.name



animal_instance = Animal("lion","roar")

animal_instance.animal_sound()

print(animal_instance)#main object at Animal X234567890