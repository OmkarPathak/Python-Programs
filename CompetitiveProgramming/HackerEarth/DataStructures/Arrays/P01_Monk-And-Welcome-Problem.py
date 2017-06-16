# Having a good previous year, Monk is back to teach algorithms and data structures. This year he welcomes the
# learners with a problem which he calls "Welcome Problem". The problem gives you two arrays A and B (each array of size N)
# and asks to print new array C such that:
# C[i]=A[i]+B[i] ;
# 1≤i≤N
# Now, Monk will proceed further when you solve this one. So, go on and solve it :)
#
# Input:
# First line consists of an integer N, denoting the size of A and B.
# Next line consists of N space separated integers denoting the array A.
# Next line consists of N space separated integers denoting the array B.
#
# Output:
# Print N space separated integers denoting the array C.
#
# Input Constraints:
# 1≤N≤100000
# 1≤A[i]≤100000;
# 1≤i≤N
# 1≤B[i]≤100000;
# 1≤i≤N
#
# SAMPLE INPUT
# 5
# 1 2 3 4 5
# 4 5 3 2 10
#
# SAMPLE OUTPUT
# 5 7 6 6 15

n = int(input())
arrayA = input().split()
arrayB = input().split()
arrayC = []
for i in range(n):
    arrayC.append(int(arrayA[i]) + int(arrayB[i]))

print(' '.join([str(i) for i in arrayC]))
