class Animal:
    #define how the animal looks, by initialising
    #create methods for this class object

    def __init__(self):     # the animals will look like this, or have these features
        self.alive = True
        self.eyes = True
        self.lungs = True
        self.skeleton = True
        self.num_legs = [0,4]
        self.heart_chambers = 1

    def breathing(self):
        print("BRREAAATHEE")

    def eat(self):
        print("EAT EAT EAT")

    def __dying(self):
        print("urhhhhh")

    def ageing(self):
        print("im ageing!")
        self.__dying() ## can only call the __dying (which is encapsulated) like this.


cat = Animal()
cat.breathing()
cat.eat()
cat.ageing()
