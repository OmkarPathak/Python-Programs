# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned
# a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where
# she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.
#
# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
# 1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the
# number of steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.
#
# Output:
# Print the required array.
#
# Constraints:
# 1≤T≤20
# 1≤N≤105
# 0≤K≤106
# 0≤A[i]≤106
#
# SAMPLE INPUT
# 1
# 5 2
# 1 2 3 4 5
#
# SAMPLE OUTPUT
# 4 5 1 2 3

from collections import deque
testCases = int(input())
for _ in range(testCases):
    n, k = map(int, input().split())
    myArray = input().split()
    myArray = deque(myArray)
    myArray.rotate(k)
    print(' '.join(myArray))

# second method
for _ in range(int(input())):
    n,sd=map(int,input().split())
    ls=input().split()
    print(" ".join(ls[n-(sd%n):]+ls[:n-(sd%n)]))
    print("\n")
