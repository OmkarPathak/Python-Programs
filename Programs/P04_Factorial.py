#Author: OMKAR PATHAK
#This program finds the factorial of the given number.
#For example, factorial of the number 5 = 5*4*3*2*1 = 120

def factorial(number):
    "the function factorial takes 'number' as an argument and returns the factorial of the given number"
    if number < 0:
        # factorial of a negative number cannot be found hence the code outputs the below string so that the user knows that he gave negative number as an input.
        print('Invalid entry! Cannot find factorial of a negative number')
    if number == 0 or number == 1:
        return 1 #if number is 0 or 1 then the factorial of these numbers is 1.
    else:
        return number * factorial(number - 1)
    #if the number is not zero,one or a negative number then the function computes and returns the above string.

if __name__ == '__main__':
    userInput = int(input('Enter the Number to find the factorial of: '))
    print(factorial(userInput))
