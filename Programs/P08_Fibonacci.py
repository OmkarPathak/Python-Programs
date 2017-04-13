#Author: OMKAR PATHAK
#This program calculates the fibonacci series till the n-th term

def fibonacci(number):
    '''This function calculates the fibonacci series till the n-th term'''
    if number <= 1:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))

def fibonacciFor(number):
    '''This function calculates the fibonacci series for n-th term using loop'''
    # first two terms
    n1 = 0
    n2 = 1
    count = 2
    if number <= 0:
        print("Please enter a positive integer")
    elif number == 1:
        print("Fibonacci sequence upto ",number,":")
        print(n1)
    else:
        print("Fibonacci sequence upto ",number,":")
        print(n1,n2,end=' ')
        while count <= number:
            nth = n1 + n2
            print(nth,end=' ')
            # update values
            n1 = n2
            n2 = nth
            count += 1

if __name__ == '__main__':
    userInput = int(input('Enter the number upto which you wish to calculate fibonnaci series: '))
    for i in range(userInput + 1):
        print(fibonacci(i),end=' ')

    print("\nUsing LOOP:")
    fibonacciFor(userInput)
