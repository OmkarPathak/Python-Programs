# Mike is crazy about collecting stamps. He is an active member of Stamp Collecting Сommunity(SCC).
#
# SCC consists of N members which are fond of philately. A few days ago Mike argued with the others from
# SCC. Mike told them that all stamps of the members could be divided in such a way that i'th member would
# get i postage stamps. Now Mike wants to know if he was right. The next SCC meeting is tomorrow. Mike still
# has no answer.
#
# So, help Mike! There are N members in the SCC, i'th member has Ci stamps in his collection. Your
# task is to determine if it is possible to redistribute C1 + C2 + ... + Cn stamps among the members of
# SCC thus that i'th member would get i stamps.
#
# Input
# The first line contains one integer N, denoting the number of members of SCC.
#
# The second line contains N integers Ci, denoting the numbers of the stamps in the collection of i'th
# member.
#
# Output
# The first line should contain YES, if we can obtain the required division, otherwise NO.
#
# Constraints
# 1 ≤ N ≤ 100 000;
#
# 1 ≤ Ci ≤ 109.
#
# Examples
# Input:
# 5
# 7 4 1 1 2
#
# Output:
# YES
#
# Input:
# 5
# 1 1 1 1 1
#
# Output:
# NO

numberOfMembers =  int(input())
C = input().split()
C = [int(i) for i in C]
result = sum(C)
check = 0
for i in range(1, len(C) + 1):
    check = check + i
if check == result:
    print('YES')
else:
    print('NO')
