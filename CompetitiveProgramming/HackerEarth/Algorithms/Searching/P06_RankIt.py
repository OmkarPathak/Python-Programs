# You have been given an array A consisting of N integers. All the elements in this array A are unique. You have to
# answer some queries based on the elements of this array. Each query will consist of a single integer x. You need to
# print the rank based position of this element in this array considering that the array is 1 indexed. The rank
# based position of an element in an array is its position in the array when the array has been sorted in ascending order.
#
# Note: It is guaranteed that all the elements in this array are unique and for each x belonging to a query, value ′x′
# shall exist in the array
#
# Input Format
#
# The first line consists of a single integer N denoting the size of array A. The next line contains N unique integers,
# denoting the content of array A. The next line contains a single integer q denoting the number of queries. Each of
# the next q lines contains a single integer x denoting the element whose rank based position needs to be printed.
#
# Output Format
#
# You need to print q integers denoting the answer to each query.
#
# Constraints
#
# 1≤N≤105
# 1≤A[i]≤109
# 1≤q≤105
# 1≤x≤109
#
# SAMPLE INPUT
# 5
# 1 2 3 4 5
# 5
# 1
# 2
# 3
# 4
# 5
#
# SAMPLE OUTPUT
# 1
# 2
# 3
# 4
# 5

n = int(input())
array = [int(i) for i in input().split()]
array.insert(0, 0)
array.sort()
q = int(input())

def binarySearch(low, high, element):
  while(low <= high):
    mid = (low + high) // 2
    if array[mid] == element:
      return mid
    elif array[mid] < element:
      low = mid + 1
    else:
      high = mid - 1

for i in range(q):
  number = int(input())
  print(binarySearch(0,len(array), number))
