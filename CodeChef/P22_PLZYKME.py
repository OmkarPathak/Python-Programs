# In a far away dystopian world, the measure of the quality of a person’s life is the numbers of likes he gets for an article
# about their life. For a person to stay alive, he has to acquire at least L number of likes before D days pass.
#
# People in this world employ various techniques to increase the number of likes. One of the famous ones is to dis-like and
# re-like their own article once per day. On doing so you can assume that the number of likes for the post increase by a
# constant factor C.
#
# So if one starts with S likes on Day-1, he would have D2 = S + C * S likes on Day-2, D3 = D2 + D2 * C on Day-3 etc. You
# are to answer if the person would survive at the end of Day-D or not.
#
# Input
#
# First line contains a single positive integer T denoting the number of test cases. The following T lines represent a test
# case each. Each test case contains 4 space-separated integers L, D, S and C.
#
# Output
#
# For each test case, print a single line containing “ALIVE AND KICKING” if the person would live, otherwise print,
# “DEAD AND ROTTING”.
#
# Constraints
#
# 1 <= T <= 1000
# 1 <= L <= 1000000000
# 1 <= D <= 1000000000
# 1 <= S <= 1000000000
# 1 <= C <= 1000000000
# Sample cases:
#
# Input
# 2
# 5 1 5 1
# 10 2 2 2
#
# Output
# ALIVE AND KICKING
# DEAD AND ROTTING
# Explanation
#
# In the first case by the end of Day-1 we would be having S that is 5 number of likes, as it is ≥ L, the answer is ALIVE AND KICKING.
#
# In the second case, D2 =S + C*S, therefore D2 = 2 + 2 * 2 = 6, as 6 is less than 10, the answer is DEAD AND ROTTING.

for i in range(int(input())):
        L, D, S, C = map(int,input().split())
        for j in range(1, D):
                S = S + C * S
                if S >= L:
                        break
        if L <= S:
                print("ALIVE AND KICKING")
        else:
                print("DEAD AND ROTTING")  
