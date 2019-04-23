from OOP import Animal

class Mammal(Animal):


    def __init__(self):

        self.fur = True
        self.hair = True
        self.backbone = True
        self.warm_blooded = True
        self.heart_chambers = 4

    def hunt(self):
        print("im hungry, need to go hunt for some food")

    def rawrr(self):
        print("rawwrrrr")


# lion = Mammal()
# lion.hunt()
# lion.rawrr()








