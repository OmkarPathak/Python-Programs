# Author: OMKAR PATHAK
# In this example, we will be seeing some more concepts of decorators such as
# property decorator, getters and setters methods.

class BankAccount(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property                   # property decorator
    def fullName(self):
        return self.firstName + ' ' + self.lastName

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName

if __name__ == '__main__':
    acc = BankAccount('Omkar', 'Pathak')
    print(acc.fullName)              # Notice that we can access the method for our class BankAccount without
                                     # parenthesis! This is beacuse of property decorator

    # acc.fullName = 'Omkar Pathak'    #This throws an error! Hence setter decorator should be used.
    acc.fullName = 'Jagdish Pathak'
    print(acc.fullName)
