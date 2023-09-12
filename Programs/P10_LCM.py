#Author: OMKAR PATHAK
#This program calculates the LCM of the two numbers entered by the user

def LCM(number1, number2):
    '''This function calculates LCM of two numbers inputed by the user'''
    max = max(number1, number2)
    while True:
        if (not max % number1 and not max % number2):
            break
        i += maximum

    return i

if __name__ == '__main__':
    userInput1 = int(input('Enter first number: '))
    userInput2 = int(input('Enter second number: '))
    print('LCM of {userInput1} and {userInput2} is {LCM(userInput1, userInput2)})
