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

userInput = int(input())
for i in range(2, userInput):
    check = 0
    for j in range(2, i):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        print(i, end = ' ')
