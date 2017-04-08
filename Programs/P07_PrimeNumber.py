#This program checks whether the entered number is prime or not

def checkPrime(number):
    '''This function checks for prime number'''
    if number == 2:
        print(number, 'is a Prime Number')
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'is not a Prime Number')
                break
            else:
                print(number, 'is a Prime Number')
                break
    else:
        print(number, 'is not a Prime Number')

if __name__ == '__main__':
    userInput = int(input('Enter a number to check: '))
    checkPrime(userInput)
