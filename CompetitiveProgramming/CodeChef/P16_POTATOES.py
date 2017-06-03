# Farmer Feb has three fields with potatoes planted in them. He harvested x potatoes from the first field, y potatoes
# from the second field and is yet to harvest potatoes from the third field. Feb is very superstitious and believes that if
# the sum of potatoes he harvests from the three fields is a prime number (http://en.wikipedia.org/wiki/Prime_number), he'll
# make a huge profit. Please help him by calculating for him the minimum number of potatoes that if harvested from the third
# field will make the sum of potatoes prime. At least one potato should be harvested from the third field.
#
# Input
# The first line of the input contains an integer T denoting the number of test cases. Each of the next T lines contain 2 integers
# separated by single space: x and y.
#
# Output
# For each test case, output a single line containing the answer.
#
# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ x ≤ 1000
# 1 ≤ y ≤ 1000
#
# Example
# Input:
# 2
# 1 3
# 4 3
#
# Output:
# 1
# 4

def isPrime(x):
    i = 2
    while (i < x):
        if (x%i == 0):
            return False
        i += 1
    return True

def check(n):
    c = 1
    while not(isPrime(c+n)):
        c += 1
    return c

testCases = int(input())
while testCases:
    testCases -= 1
    x,y = map(int,input().split())
    n = x + y
    print (check(n))
