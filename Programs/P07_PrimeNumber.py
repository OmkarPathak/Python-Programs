#Author: OMKAR PATHAK
#This program checks whether the entered number is prime or not

def checkPrime(number):
    '''This function checks for prime number'''

    for i in range(2, (number // 2) + 1):
        if not number % i:
            print(f"{number} is not a Prime Number.")
            return

    print(f"{number} is a Prime Number")

if __name__ == '__main__':
    userInput: int = int(input('Enter a number to check: '))
    checkPrime(userInput)
