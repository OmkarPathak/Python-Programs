#Author: OMKAR PATHAK
#This program calculates the factorial of a given number

def factorial(number):
    '''This function calculates the factorial of a number'''
    if number in (0, 1):
        return 1
    else:
        return number * factorial(number - 1)

def factorial_without_recursion(number):
    fact: int = 1
    num: int = number

    while number:
        fact *= number
        number -= 1
    print(f"Factorial of {num} is: {fact}")

if __name__ == '__main__':
    userInput: int = int(input('Enter the number to find its factorial: '))
    print(f"Factorial of {userInput} is: {factorial(userInput)}")
    factorial_without_recursion(userInput)
