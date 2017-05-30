# Banknotes in the state of Strangeland don't have any regulated values like 1, 5, 10, 20, 50, 100, etc. In fact, it's
# possible to see any positive integer on a banknote of Strangeland. Indeed, this isn't the most convenient thing.
#
# Ann is working as a sweet seller at a shop in Strangeland. Every kind of sweets in this shop has its own cost, and
# sweets of the same kind have the same cost.
#
# Customers in Strangeland are strange. A customer points at some kind of sweets and gives several banknotes to the
# seller. This means that he wants to buy a positive number of sweets of that kind. He doesn't tell the exact number of
# sweets he wants to buy. The only thing Ann knows is: an 'adequate' customer won't give any extra banknotes. It means that
# if you throw away any banknote, the resulting amount of money won't be enough to buy the wanted number of sweets.
#
# Ann has to determine the number of sweets the customer wants. Help Ann write a program which determines this number or
# tells that it's impossible.
#
# Input
# The first line of the input contains a single integer T, the number of test cases (no more than 20). T test cases follow.
# Each test case consists of two lines. The first of these lines contains two integers N and X (1 ≤ N, X ≤ 100) separated by
# a single space. N is the number of banknotes given by the customer. X is the cost of a single sweet of the chosen kind.
# The second of these lines contains N space-separated integers Ai (1 ≤ Ai ≤ 100), the values of the banknotes.
#
# Output
# For each test case output exactly one line containing a single integer:
#
# -1 if the customer is inadequate and has given extra banknotes, or
# K, the number of sweets the customer wants to buy. If there are several possible answers, output the largest of them.
#
# Example
#
# Input:
# 3
# 4 7
# 10 4 8 5
# 1 10
# 12
# 2 10
# 20 50
#
# Output:
# -1
# 1
# 7

testCases = int(input())
while testCases:
    testCases -= 1
    N, X = map(int, input().split())
    bankNotes = [int(i) for i in input().split()]
    bankNotes = sum(bankNotes)
    if (X) <= bankNotes:
        result = bankNotes // (X)
        if result >= N:
            print(result)
        else:
            print(-1)
    else:
        print(-1)
