# Please compute the sum of squares for the given numbers: a, a+1, ..., b-1, b.
#
# Input
#
# Two numbers: a and b separated by space, where 1 <= a <= b <=100.
#
# Output
#
# Computed sum: a*a + (a+1)*(a+1) + ... + (b-1)*(b-1) + b*b
#
# Example
#
# Input:
# 1 4
# # Please compute the sum of squares for the given numbers: a, a+1, ..., b-1, b.
#
# Input
#
# Two numbers: a and b separated by space, where 1 <= a <= b <=100.
#
# Output
#
# Computed sum: a*a + (a+1)*(a+1) + ... + (b-1)*(b-1) + b*b
#
# Example
#
# Input:
# 1 4
#
# Output:
# 30
# Example 2
#
# Input:
# 5 6
#
# Output:
# 61
# Output:
# 30
# Example 2
#
# Input:
# 5 6
#
# Output:
# 61

a, b = map(int, input().split())
result = 0
for i in range(a, b + 1):
    result += i*i
print(result)
