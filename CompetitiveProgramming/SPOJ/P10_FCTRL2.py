# You are asked to calculate factorials of some small positive integers.
#
# Input
#
# An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n,
# 1<=n<=100.
#
# Output
#
# For each integer n given at input, display a line with the value of n!
#
# Example
#
# Sample input:
# 4
# 1
# 2
# 5
# 3
# Sample output:
#
# 1
# 2
# 120
# 6

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

testCases = int(input())
for _ in range(testCases):
    number = int(input())
    print(factorial(number))
