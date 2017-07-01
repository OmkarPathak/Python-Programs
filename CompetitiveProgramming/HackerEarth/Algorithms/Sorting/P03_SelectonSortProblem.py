# Selection Sort Problem
#
# Consider an Array a of size N
# Iterate from 1 to N
# In ith iteration select the ith minimum and swap it with a[i]
# You are given an array a, size of the array N and an integer x.
# Follow the above algorithm and print the state of the array after x iterations have been performed.
#
# Input Format
#
# The first line contains two integer N and x denoting the size of the array and the steps of the above algorithm to be
# performed respectively. The next line contains N space separated integers denoting the elements of the array.
#
# Output Format
#
# Print N space separated integers denoting the state of the array after x steps
#
# Constraints
#
# 1≤N≤100
# 1≤a[i]≤100
# 1≤x≤N
#
# SAMPLE INPUT
# 5 2
# 1 2 3 4 5
#
# SAMPLE OUTPUT
# 1 2 3 4 5

n, x = map(int, input().split())
array = [int(i) for i in input().split()]
for i in range(x):              # Note x here, this is what yields the required result
    minimum = i
    for j in range(i + 1, n):
        if array[j] < array[minimum]:
            minimum = j
    if(minimum != i):
        array[i], array[minimum] = array[minimum], array[i]
    if(i == x):
        break

print(' '.join([str(i) for i in array]))
