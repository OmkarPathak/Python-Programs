# Given an array A on size N, you need to find the number of ordered pairs (i,j) such that i<j and A[i]>A[j].
#
# Input:
# First line contains one integer, N, size of array.
# Second line contains N space separated integers denoting the elements of the array A.
#
# Output:
# Print the number of ordered pairs (i,j) such that i<j and A[i]>A[j].
#
# Constraints:
# 1≤N≤106
# 1≤A[i]≤106
#
# SAMPLE INPUT
# 5
# 1 4 3 2 5
#
# SAMPLE OUTPUT
# 3

n = int(input())
array = [int(i) for i in input().split()]

def mergeSort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
        return merge(left, right)

def merge(left, right):
    mergeArray = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            mergeArray.append(left[0])
            left.remove(left[0])
        else:
            mergeArray.append(right[0])
            right.remove(right[0])
            global value
            value += 1                  # Note this step
    if len(left) == 0:
        mergeArray += right
    else:
        mergeArray += left

    return mergeArray

value = 0
mergeSort(array)
print(value)
