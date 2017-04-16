#Author: OMKAR PATHAK
#This example shows the use of __init__ constructor

class Vehicle():
    #__init__ is used to set values as soon as new object are created
    #__init__ is a keyword hence it has to be named like it is
    def __init__(self):     #called automatically hence known as magic method
        print('Calling init')
        self.val = 0
        self.cost = 10000   #Setting the default value when the object is created

    def incrementVehicle(self):
        self.val += 1


car = Vehicle()     #__init__ is called
print('First obj value:',car.val)
car.incrementVehicle()
car.incrementVehicle()
print('First obj value after incrementing:',car.val)      #2

bike = Vehicle()       #__init__ is called makes val 0 for this ANOTHER instance
print('Second obj value:',bike.val)
