#Author: OMKAR PATHAK
#In this example we will be seeing how instance Attributes are used
#Instance attributes are accessed by: object.attribute
#Attributes are looked First in the instance and THEN in the class

import random
class Vehicle():
    #Class Methods/ Attributes
    def type(self):
        #NOTE: This is not a class attribute as the variable is binded to self. Hence it becomes
        #instance attribute
        self.randomValue = random.randint(1,10) #Setting the instance attribute

car = Vehicle()
car.type()              #Calling the class Method
print(car.randomValue)  #Calling the instance attribute
