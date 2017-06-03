# This time your task is simple.
#
# Given two integers
# X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.
#
# Input:
# First line of the input contains two integers X and K separated by a single space.
#
# Output:
# Print the largest number formed in a single line.
#
# Constraints:
#
# 1 ≤ X ≤ 1018
# 0 ≤ K ≤ 9
#
# SAMPLE INPUT
# 4483 2
#
# SAMPLE OUTPUT
# 9983

N, K = input().split()
change = '9'
N = list(N)
for i in range(int(K)):
    N[i] = change

print(''.join([str(i) for i in N]))
