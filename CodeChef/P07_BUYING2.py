# Customers in Strangeland are strange. A customer points at some kind of sweets and gives several banknotes
# to the seller. This means that he wants to buy a positive number of sweets of that kind. He doesn't tell
# the exact number of sweets he wants to buy. The only thing Ann knows is: an 'adequate' customer won't give
# any extra banknotes. It means that if you throw away any banknote, the resulting amount of money won't be
# enough to buy the wanted number of sweets.
#
# Ann has to determine the number of sweets the customer wants. Help Ann write a program which determines
# this number or tells that it's impossible.
#
# Input
# The first line of the input contains a single integer T, the number of test cases (no more than 20).
# T test cases follow. Each test case consists of two lines. The first of these lines contains two integers
# N and X (1 ≤ N, X ≤ 100) separated by a single space. N is the number of banknotes given by the customer.
# X is the cost of a single sweet of the chosen kind. The second of these lines contains N space-separated
# integers Ai (1 ≤ Ai ≤ 100), the values of the banknotes.
#
# Output
# For each test case output exactly one line containing a single integer:
#
# -1 if the customer is inadequate and has given extra banknotes, or
# K, the number of sweets the customer wants to buy. If there are several possible answers, output the
# largest of them.
#
# Example
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
#
# Explanation
# In the first test case, the total amount of money received from the customer is 27. He can't buy more than
# 3 sweets with this amount. If you throw away the banknote of value 5 (or of value 4), it will still be
# possible to buy 3 sweets. Hence the customer is inadequate.
#
# In the second test case, it's clear that he wants to buy just one sweet (note that this number should be
# positive).
#
# In the third test case, the total amount of money received is 70, which is enough for 7 sweets. The
# customer might want to buy only 6 sweets, but we are interested in the largest possible answer.
testCases = int(input())
while testCases:
    testCases -= 1
    N, X = map(int, input().split())
    bankNotes = [int(i) for i in input().split()]
    bankNotes = sum(bankNotes)
    if (N * X) <= bankNotes:
        result = bankNotes // X
        print(int(result))
    else:
        print(int('-1'))
