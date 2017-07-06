# Author: OMKAR PATHAK

# In this program we will learn what Python lambda is.
# The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without
# a name. These functions are throw-away functions, i.e. they are just needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). The lambda
# feature was added to Python due to the demand from Lisp programmers.

# The argument list consists of a comma separated list of arguments and the expression is an arithmetic
# expression using these arguments. You can assign the function to a variable to give it a name.
# The following example of a lambda function returns the sum of its two arguments:

myFunc = lambda x, y: x * y
# returns 6
print(myFunc(2, 3))

# example to find squares of all numbers from a list
myList = [i for i in range(10)]
# returns square of each number
myFunc = lambda x: x * x

squares = list(map(myFunc, myList))
print(squares)              # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
