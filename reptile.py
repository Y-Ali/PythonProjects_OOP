from OOP import Animal

#this is inheritance. We are importing the code (or properties) from the OOP.py (code) file.
#creates a Reptile with its own properties, as well as properties of an animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()    # this line of code needs to be here to initialise as an Animal
        self.cold_blooded = True
        self.lay_eggs = True
        self.heart_chambers = [3,4]

        self.speed = 100

    def seek_heat(self):
        print("Need to gain energy from the sun")

    def hunt(self):
        print("wait.....wait for it....")

lizard = Reptile()
lizard.hunt()
lizard.seek_heat()
print(lizard.cold_blooded) # to see if its cold blooded.
