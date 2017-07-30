#Author: OMKAR PATHAK
#This program calculates the fibonacci series till the n-th term

def fibonacci(number):
    '''This function calculates the fibonacci series till the n-th term'''
    if number <= 1:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))

def fibonacci_without_recursion(number):
    if number == 0: return 0
    fibonacci0, fibonacci1 = 0, 1
    for i in range(2, number + 1):
        fibonacci1, fibonacci0 = fibonacci0 + fibonacci1, fibonacci1
    return fibonacci1

if __name__ == '__main__':
    userInput = int(input('Enter the number upto which you wish to calculate fibonnaci series: '))
    for i in range(userInput + 1):
        print(fibonacci(i),end=' ')

    print("\nUsing LOOP:")
    print(fibonacci_without_recursion(userInput))
