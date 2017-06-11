# Nestor was doing the work of his math class about three days but he is tired of make operations a lot and he should
# deliver his task tomorrow. His math’s teacher gives him two numbers a and b. The problem consist of finding the last
# digit of the potency of base a and index b. Help Nestor with his problem. You are given two integer numbers: the base
# a (0 <= a <= 20) and the index b (0 <= b <= 2,147,483,000), a and b both are not 0. You have to find the last digit
# of ab.
#
# Input
#
# The first line of input contains an integer t, the number of test cases (t <= 30). t test cases follow. For each test
# case will appear a and b separated by space.
#
# Output
#
# For each test case output an integer per line representing the result.
#
# Example
#
# Input:
# 2
# 3 10
# 6 2
#
# Output:
# 9
# 6

testCases = int(input())
while testCases:
    testCases -= 1
    a,b = map(int,input().split())
    if b <= 4:
        print(str(pow(a,b))[-1])
    else:
        if b % 4:
            print(str(pow(a,b%4))[-1])
        else:
            print(str(pow(a,4))[-1])
