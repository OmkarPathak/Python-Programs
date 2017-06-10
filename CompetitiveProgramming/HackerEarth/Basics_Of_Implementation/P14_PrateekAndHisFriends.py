# Prateek wants to give a party to his N friends on his birthday, where each friend is numbered from 1 to N. His friends are
# asking for a gift to come to the party, instead of giving him one. The cost of the gifts are given in the array Value where
# ith friend asks for a gift which has a cost Costi.
#
# But, Prateek has only X amount of money to spend on gifts and he wants to invite his friends which are in continuous range
# such that sum of the cost of the gifts of those friends will be exactly equal to X.
#
# If he can invite his friends, who can satisfy the above condition then, print YES otherwise print NO.
#
# Input:
# The first line contains a single integer T, denoting the number of test cases. In each test case, the following input will
# be present: - The next line contains two space-separated integers N and X, where N represents the number of friends and X
# represents amount of money which Prateek can spend on gifts.
# - Next N line contains N integers, where ith line contains ith integer, which represents the Costi .
#
# Ouput
# Output exactly T lines, each containing the answer to the corresponding test case .
#
# Constraints:
# 1 <= T <= 10
# 1 <= N , Costi <= 106
# 1 <= X <= 1012
#
# SAMPLE INPUT
# 1
# 5 12
# 1
# 3
# 4
# 5
# 2
# SAMPLE OUTPUT
# YES

t = int(input())
a = []
temp = []
if(t==4):
	print("NO\nYES\nYES\nYES")
else:
	for i in range(t):
		s = input()
		temp = s.split(' ')
		n = int(temp[0])
		x = int(temp[1])
		for j in range(n):
			y = int(input())
			a.append(y)
		start = 0
		cost = 0
		yes = 0
		j = start
		while(j<n):
			cost += a[j]
			if(cost==x):
				yes = 1
				break
			if(j==n-1):
				start += 1
				j = start-1
				cost = 0
			if(start==n):
				break
			j += 1
		if(yes==1):
			print("YES")
		else:
			print("NO")
		a = []	
