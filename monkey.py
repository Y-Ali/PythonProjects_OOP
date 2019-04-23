from mammal import Mammal

class Monkey(Mammal):

    def __init__(self):
        self.tail = True
        self.num_legs = 2


    def swing(self):
        print("I like to swing on trees!")

    def eat(self):
        print("Bananas")


    def speak(self):
        print("im a monkey")



# m = Monkey()
# m.swing()
# m.eat()
#m.speak()

