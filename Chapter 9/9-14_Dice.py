from random import randint

class Die():

    def __init__(self, number_sides):
        self.number_sides = number_sides
    
    def roll_die(self):
        print("The die has " + str(self.number_sides) + " sides.") 
        print("Rolling the die...")
        print(randint(1, self.number_sides))

#six_sided = Die(6)
#six_sided.roll_die()

#ten_sided = Die(10)
#ten_sided.roll_die()

twenty_sided = Die(20)
twenty_sided.roll_die()