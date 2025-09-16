

# SuperHero (name,super_powers,universe)


class SuperHero:

    name:str

    super_powers:str

    universe:str


    def set_super_hero(self,name,super_powers,universe):

        self.name = name

        self.super_powers = super_powers

        self.universe = universe

    def display_super_hero(self):

        print(self.name,self.super_powers,self.universe)


batman_instance = SuperHero()

batman_instance.set_super_hero("BATMAN","fly,run,rich","dc")

minnal_muraly_instance = SuperHero()

minnal_muraly_instance.set_super_hero("minnalmuraly","run,strength","basiluniverse")

minnal_muraly_instance.display_super_hero()

