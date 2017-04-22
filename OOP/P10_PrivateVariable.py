# Author: OMKAR PATHAK
# In this example we will see how the private variables work in Python

class Person(object):
    def __init__(self, name):
        self.name = name
        self.__education = 'Engineering'         # Private Variable

    def displayInfo(self):
        name = self.name
        education = self.__education             # Can only be accessed within the class
        print('My name is', name, 'and I have completed my', education)

if __name__ == '__main__':
    myObj = Person('Omkar')
    myObj.displayInfo()
    print(myObj.name)                           # Can be accessed as it is public variable
    # print(myObj.__education)                  # Throws an error
    print(myObj._Person__education)             # Private variable can be accessed like this but NEVER EVER
                                                # do this please!!!
