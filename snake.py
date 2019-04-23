from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()

        self.scales = True                             #Abstraction - features of the snake.
        self.venom = True
        self.heart_chambers = [2,4]                    #Polymorphism
        self.cold_blooded = True

    def animal_speed(self):
        print("The snakes speed is",(self.speed))

    def hiss(self):
        print("ssssssssssss...")

    def shred_skin(self):
        print("i'm shredding my skin")

cobra = Snake()
cobra.speed = 10
cobra.animal_speed()
print(cobra.heart_chambers)
cobra.seek_heat()   #from Reptile class (inheritance)
cobra.hunt()        #from Reptile class (inheritance)
cobra.eat()         #from Animal class
cobra.breathing()
cobra.shred_skin()







