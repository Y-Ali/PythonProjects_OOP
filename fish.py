from OOP import Animal

class Fish:


    def __init__(self):     # the animals will look like this, or have these features
        self.backbone = True
        self.eyes = True
        self.lungs = True
        self.num_legs = [0]
        self.lay_eggs = True
        self.gills = True

    def breathing(self):
        print("I breathe through my mouth and out my gills")

    def swim(self):
        print("just keep swimming just keep swimming")


# whale = Fish()
# whale.breathing()
