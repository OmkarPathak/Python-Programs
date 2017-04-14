#Author: OMKAR PATHAK
#This program converts the given binary number to its decimal equivalent

def binaryToDecimal(binary):
    '''This function calculates the decimal equivalent to given binary number'''
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print('Decimal equivalent of {} is {}'.format(binary1, decimal))

if __name__ == '__main__':
    userInput = int(input('Enter the binary number to check its decimal equivalent: '))
    binaryToDecimal(userInput)
