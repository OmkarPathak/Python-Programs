# You have been given an array A of size N consisting of positive integers. You need to find and print the product of all
# the number in this array Modulo (10^9+7).
#
# Input Format:
# The first line contains a single integer N denoting the size of the array. The next line contains N space separated
# integers denoting the elements of the array
#
# Output Format:
# Print a single integer denoting the product of all the elements of the array Modulo
#
# Constraints:
# 1 ≤ N ≤ 103
# 1 ≤ A[i] ≤ 103

# Sample Input:
# 5
# 1 2 3 4 5
#
# Sample Output:
# 120

modulo = (10 ** 9 + 7)
result = 1
testCases = int(input())
List = [int(i) for i in input().split()]
for i in List:
    result = result * i % modulo

print(result)
