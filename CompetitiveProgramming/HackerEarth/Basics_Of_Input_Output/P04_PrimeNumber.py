# You are given an integer N. You need to print the series of all prime numbers till N.
#
# Input Format
#
# The first and only line of the input contains a single integer N denoting the number till where you need to find the
# series of prime number.
#
# Output Format
#
# Print the desired output in single line separated by spaces.
#
# Constraints
# 1 <= N <=1000

import math

userInput = int(input())
if userInput > 2:
    print("2",end = ' ')
for i in range(3, userInput + 2):
    check = 0
    for j in range(2, int(math.sqrt(i))+ 1):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        print(i, end = ' ')
