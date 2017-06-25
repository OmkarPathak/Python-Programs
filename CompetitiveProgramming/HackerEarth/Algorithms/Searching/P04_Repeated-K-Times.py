# Given a List of N number a1,a2,a3........an, You have to find smallest number from the List that is repeated in the
# List exactly K number of times.
#
# Input Format
#
# First Line of Input Contain Single Value N, Size of List
# Second Line of Input Contain N Space Separated Integers
# Third Line of Input Contain Single Value K
#
# Output Format
#
# Smallest Integer Value That is Repeated Exactly K Number of Time
#
# Constraints
#
# 0 < N < 100001
# 0 < K < 100001
# 0 < ai < 100001
#
# NOTE
# There Will Be Atleast One Variable Which Is Repeated K Times
#
# SAMPLE INPUT
# 5
# 2 2 1 3 1
# 2
#
# SAMPLE OUTPUT
# 1

n = int(input())
array = [int(i) for i in input().split()]
arrayCheck = list(set(array))
k = int(input())
nos = []
count = 0
for i in range(len(arrayCheck)):
    count = array.count(arrayCheck[i])
    if count == k:
        nos.append(arrayCheck[i])

nos.sort()
print(nos[0])
