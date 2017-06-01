# It is winter super sale and all the shops have various offers. Suraj selected N items to buy and he is standing in the
# billing queue. It was then he noticed the offer "Buy two, get two". That means for every two items you buy, they give you
# two items for free. However, items can be of varying price, they always charge for 2 most costly items and give other 2 as
# free. For example, if the items cost 1, 1, 2, 2, then you have to pay 4 and take all 4 items.
#
# Suraj is busy reordering his items to reduce the total price he has to pay. He can separate the items and get them on
# different bills if needed. Can you tell me what is the least price Suraj has to pay to buy all the N items?
#
# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases
# follows. First line of each test case has single integer N. Second line of each test case has N space separated integers,
# which are the costs of items Suraj want to buy.
#
# Output
# For each test case, output a single line containing the required answer.
#
# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000
# 1 ≤ Cost of items ≤ 1000
# Example
# Input:
# 3
# 4
# 1 1 2 2
# 2
# 10 200
# 7
# 1 1 10 2 2 2 1
#
# Output:
# 4
# 210
# 14

testCases = int(input())
while  testCases:
    testCases -= 1
    N = int(input())
    items = [int(i) for i in input().split()]
    items.sort()
    result = 0
    while items:
        if len(items) >= 4:
            result += sum(items[-2:])
            items = items[:-4]
        elif len(items) == 3:
            result += sum(items[-2:])
            break
        elif len(items) == 2:
            result += sum(items)
            break

    print(result)
