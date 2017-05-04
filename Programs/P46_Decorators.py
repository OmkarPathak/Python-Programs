# Author: OMKAR PATHAK
# In this example program we will see how decorators work in Python

def decorator(myFunc):
    def insideDecorator(*args):
        print('insideDecorator Function executed before {}'.format(myFunc.__name__))
        return myFunc(*args)
    return insideDecorator

@decorator      # Decorator function that takes below function as an argument
def display(*args):
    '''  This function is passed as an argument to the decorator function specified above after @ sign '''
    print('In display function')
    print(*args)

display('Hello','Hi',123)
