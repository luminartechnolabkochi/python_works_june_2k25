

class Father:

    def cricket_skills(self):

        print("father cricket skills")

    

class Mother:

    def cooking_skills(self):

        print("mother cooking skills")


class Child(Mother,Father):

    def learninng_skills(self):

        print("child learning skills")


child_instance = Child()

child_instance.learninng_skills()

child_instance.cooking_skills()

child_instance.cricket_skills()

"""
constructor
__str__
inheritance



"""