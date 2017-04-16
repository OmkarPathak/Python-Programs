#Author: OMKAR PATHAK
#In this example we will be seeing how instance methods are used
#Instance methods are accessed by: instance.method()

class Vehicle():
    #Class Methods/ Attributes

    #Here self is passed as an argument because instance is passed as first argument
    def type(self):     #Without self it throws an error
        print(self)
        print('I have a type')

car = Vehicle()
print(car)
car.type()
