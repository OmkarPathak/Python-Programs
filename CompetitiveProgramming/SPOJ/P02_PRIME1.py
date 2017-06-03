# Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers
# between two given numbers!
#
# Input
#
# The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two
# numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
#
# Output
#
# For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an
# empty line.
#
# Example
#
# Input:
# 2
# 1 10
# 3 5
#
# Output:
# 2
# 3
# 5
# 7
#
# 3
# 5
# Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well
# designed)

import math

N_MAX = 1000000000
LIMIT = int(math.sqrt(N_MAX)) + 1
is_prime = [True for i in range(LIMIT)]
is_prime[1] = False

for i in range(2, LIMIT):
    if is_prime[i]:
    	for j in range(i*2, LIMIT, i):
    		is_prime[j] = False

T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    m = max(m, 2)
    query = [True for x in range(m, n + 1)]

    for i in range(2, LIMIT):
    	if is_prime[i]:
    		v = ((m - 1) // i + 1) * i
    		if v == i:
    			v = i*2
    		for j in range(v, n+1, i):
    			query[j - m] = False

    for j in range(m, n + 1):
    	if query[j - m]:
    		print(j)
    print() 
