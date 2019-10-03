# Golu wants to find out the sum of Lucky numbers.Lucky numbers are those numbers which contain exactly two set bits.This task is very 
# diffcult for him.So Help Golu to find sum of those numbers which exactly contain two set bits upto a given number N.

# 3 5 10 are lucky numbers where 7 14 are not.

# INPUT
# First line contain number of test cases T.Each test case contains a single number N.
# OUTPUT
# Print sum of all Lucky Numbers upto N.Output may be large so take modulo with 1000000007.

# Constraints
# 1<=T<=105
# 1<=N<=1018

# NOTE: Since value of test cases and n is really large, please use fast I/O optimization techniques.

# SAMPLE INPUT 
# 1
# 5
# SAMPLE OUTPUT 
# 8

import collections
for _ in range(int(input())):
    
    sum = 0
    mod = 1000000007
    n = int(input())
    j = bin(n)
    bl = len(j) - 2
    
    
    while bl > 0:
        lo = bl - 2
        
        while lo >= 0:
            i = '1' + ('0' * lo) + ('1' ) + ('0' * (bl - lo - 2))
            
            if int(i,2) <= n : 
                sum = (sum +  int(i,2)) 
            lo -= 1
            
        bl -= 1
    print(sum % mod)
