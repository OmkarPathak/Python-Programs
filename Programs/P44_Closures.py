# Author: OMKAR PATHAK

# Wikipedia:
# A closure is a record storing a function[a] together with an environment:
# a mapping associating each free variable of the function (variables that are used locally, but
# defined in an enclosing scope) with the value or reference to which the name was bound when
# the closure was created.A closure—unlike a plain function—allows the function to access those
# captured variables through the closure's copies of their values or references, even when the function
# is invoked outside their scope.

def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()
