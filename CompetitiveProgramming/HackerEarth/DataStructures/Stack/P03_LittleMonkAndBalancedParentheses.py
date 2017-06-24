# Given an array of positive and negative integers, denoting different types of parentheses. The positive numbers
# xi denotes opening parentheses of type xi and negative number −xi denotes closing parentheses of type xi.
#
# Open parentheses must be closed by the same type of parentheses. Open parentheses must be closed in the correct order, i.e., never close an open pair before its inner pair is closed (if it has an inner pair). Thus,
# [1,2,−2,−1] is balanced, while [1,2,−1,−2] is not balanced.
#
# You have to find out the length of the longest subarray that is balanced.
#
# Input Format:
# First line contains an input (1≤N≤2∗105), denoting the number of parentheses. Second line contains N space separated
# integers. (−105≤xi≤105,xi≠0) denoting the ith parentheses of the array.
#
# Output Format:
# Print the length of the longest subarray that is balanced.
#
# SAMPLE INPUT
# 5
# 1 -1 2 3 -2
#
# SAMPLE OUTPUT
# 2
#
# Explanation
# The longest subarray that is balanced is (1,−1). (2,3,−2) is not balanced as (3) is not balanced

n = int(input().strip())
lst = list(map(int,input().split()))
l = []
max_balanced = 0
current_balance = 0

for element in lst:
    if element > 0:
        if current_balance > 0 and len(l):
            current_balance = 0
        l.append(element)
    elif len(l):
        peek_element = l.pop()
        if peek_element == -(element):
            current_balance += 1
        else:
            current_balance = 0
            l = []
        if current_balance > max_balanced:
            max_balanced = current_balance
print(max_balanced * 2)
