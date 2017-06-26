# You are given an array A of size N, and Q queries to deal with. For each query, you are given an integer X, and
# you're supposed to find out if X is present in the array A or not.
#
# Input:
# The first line contains two integers, N and Q, denoting the size of array A and number of queries. The second line
# contains N space separated integers, denoting the array of elements Ai. The next Q lines contain a single integer X
# per line.
#
# Output:
# For each query, print YES if the X is in the array, otherwise print NO.
#
# Constraints:
# 1 <= N, Q <= 105
# 1 <= Ai <= 109
# 1 <= X <= 109
#
# SAMPLE INPUT
# 5 10
# 50 40 30 20 10
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
#
# SAMPLE OUTPUT
# YES
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO
# NO

# Using binary search (non-efficient)
n, q = map(int, input().split())
array = [int(i) for i in input().split()]
array.insert(0, 0)
array.sort()

def binarySearch(low, high, element):
  while(low <= high):
    mid = (low + high) // 2
    try:
      if array[mid] == element:
        return mid
      elif array[mid] < element:
        low = mid + 1
      else:
        high = mid - 1
    except IndexError:
      return False

for i in range(q):
    number = int(input())
    ans = binarySearch(0,len(array), number)
    if ans:
        print('YES')
    else:
        print('NO')

# using traditional python (set as they are hashtables, hence efficient)
in_ = input().split()
arr = [x for x in input().split()]
arr =set(arr)   # since python set is a hashtable and O(n) in hashtbale is O(1)
for i in range(int(in_[1])):
    if input() in arr:
        print("YES")
    else:
        print("NO")
