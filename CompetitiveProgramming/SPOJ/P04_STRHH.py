# Given a sequence of 2*k characters, please print every second character from the first half of the sequence. Start
# printing with the first character.
#
# Input
#
# In the first line of input your are given the positive integer t (1<=t<=100) - the number of test cases. In the each of the next t lines, you are given a sequence of 2*k (1<=k<=100) characters.
#
# Output
#
# For each of the test cases please please print every second character from the first half of a given sequence
# (the first character should appear).
#
# Example
#
# Input:
# 4
# your
# progress
# is
# noticeable
#
# Output:
# y
# po
# i
# ntc
#  Submit solution!

testCases = int(input())
for _ in range(testCases):
    string = input()
    check = len(string) // 2    # split the length of string in two halves
    for i in range(0, check, 2):
        print(string[i], end = '')
    print()
