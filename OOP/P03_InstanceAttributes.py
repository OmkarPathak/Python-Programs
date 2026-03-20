# Author: OMKAR PATHAK
# Demonstration of Instance Attributes

import random

class Vehicle:

    def type(self):
        # Creating instance attribute
        self.randomValue = random.randint(1, 10)

# Creating object
car = Vehicle()

# Calling method
car.type()

# Accessing instance attribute
print("Random Value:", car.randomValue)
