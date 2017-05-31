# You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a
# positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.
#
# Input Format:
# The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.
#
# Output Format
# Output a single line denoting the factorial of the number N.
#
# Constraints
# 1 ≤ N ≤ 10

def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input())
print(factorial(number))
