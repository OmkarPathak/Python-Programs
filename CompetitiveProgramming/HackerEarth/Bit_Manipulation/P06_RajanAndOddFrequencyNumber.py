# Given an array of numbers of size (2*n+1).Raja is unable to find the number which is present odd number of times.It is guaranteed that only one such number exists.Can you help Raja in finding the number which is present odd number of times?

# Input
# First line contains value of n.
# Second line contains (2*n+1) array elements.
# Output
# Print the required number.
# Constraints
# 1≤ n ≤ 
# 1≤ a[i] ≤ 

# SAMPLE INPUT 
# 2
# 1 2 3 2 1
# SAMPLE OUTPUT 
# 3
# Explanation
# For first input only 3 is the number which is present odd number of times.

a=int(input())
b=list(map(int,input().split()))
d=b[0]
for i in range(1,len(b)):
    d=d^b[i]
print(d)
