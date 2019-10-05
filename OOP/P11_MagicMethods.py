# Author: OMKAR PATHAK
# In this example we will see what are Python Magic Methods (or Special Methods) and how to overload them
# Now why these methods are called Magic or Special methods anyway? The reason is that these
# methods are invoked directly after creation of a class instance. For example:
# __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.

class Employee(object):
    def __init__(self, firstname, lastname, salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname

    # Implements behaviour for built in type comparison to int
    def __int__(self):
        return self.salary

    # For overloading the (==)
    def __eq__(self,other):
       return self.salary==other.salary   

    # For overloading the (+)
    def __add__(self, other):
        return self.salary + other.salary

    # For overloading the (*)
    def __mul__(self, other):
        return self.salary * other.salary

if __name__ == '__main__':
    Omkar = Employee('Omkar', 'Pathak', 1000)
    Jagdish = Employee('Jagdish','Pathak', 2000)
    print(Omkar)                # Full Name: Omkar Pathak (This output because of __str__ method overloading)
    print(Jagdish)              # Full Name: Jagdish Pathak
    print(Omkar + Jagdish)      # 3000 (This output because of __add__ method overloading)
    print(Omkar * Jagdish)      # 2000000 (__mul__)
    print(int(Omkar))           # 1000 (__int__)
    print(int(Jagdish))         # 2000 (__int__)
    print(Omkar==Jagdish)
