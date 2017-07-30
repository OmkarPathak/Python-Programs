#Author: OMKAR PATHAK
#This program calculates the factorial of a given number

def factorial(number):
    '''This function calculates the factorial of a number'''
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def factorial_without_recursion(number):
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    print('Factorial of', number,'is: ')
    print(fact)

if __name__ == '__main__':
    userInput = int(input('Enter the number to find its factorial: '))
    print('Factorial of', userInput, 'is:', factorial(userInput))
    factorial_without_recursion(userInput)
