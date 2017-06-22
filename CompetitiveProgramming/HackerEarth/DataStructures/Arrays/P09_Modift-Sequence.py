# Suppose we have a sequence of non-negative integers, Namely a_1, a_2, ... ,a_n. At each time we can choose one term
# a_i with 0 < i < n and we subtract 1 from both a_i and a_i+1. We wonder whether we can get a sequence of all zeros
# after several operations.
#
# Input
#
# The first line of test case is a number N. (0 < N <= 10000) The next line is N non-negative integers, 0 <= a_i <= 109
#
# Output
#
# If it can be modified into all zeros with several operations output “YES” in a single line, otherwise output “NO”
# instead.
#
# SAMPLE INPUT
# 2
# 1 2
#
# SAMPLE OUTPUT
# NO

# Best Solution
n= int(input())
num= list(map(int, input().split(' ')))
single_num= 0
for i in range(n):
    single_num += num[i]*(10**i)
if int(single_num)%11 ==0:
    print("YES")
else:
    print('NO')

# You are subtracting 1 from both adjacent digits and you have to get zeroes. That just means the number should be
# multiple of 11.
# To better understand this, do the reverse. Take some number of zeroes like 000000 and add 1 to some pair of adjacent
# digits, in any way you like. (eg, first like 000011, then 000132, then 011132 etc). In the end, apply the test of
# divisibility of 11 to that number. You will find that the number will always be divisible by 11. That's what I did in
# the code.

# Average (lame) way
skip = input()
array = input().split()
array = [int(i) for i in array]
check = array[0]
if check == 0:
  print('YES')
elif array.count(array[0]) == len(array) and len(array) > 1:
    print('YES')
else:
    print('NO')
