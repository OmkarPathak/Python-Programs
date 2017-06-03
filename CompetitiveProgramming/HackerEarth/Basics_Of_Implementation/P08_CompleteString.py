# A string is said to be complete if it contains all the characters from a to z. Given a string, check if it complete or
# not.
#
# Input
# First line of the input contains the number of strings N. It is followed by N lines each contains a single string.
#
# Output
# For each test case print "YES" if the string is complete, else print "NO"
#
# Constraints
# 1 <= N <= 10
# The length of the string is at max 100 and the string contains only the characters a to z

# SAMPLE INPUT
# 3
# wyyga
# qwertyuioplkjhgfdsazxcvbnm
# ejuxggfsts
#
# SAMPLE OUTPUT
# NO
# YES
# NO

testCases = int(input())
while testCases:
    testCases -= 1
    string = input()
    alphabet = list(map(chr, range(97, 123)))
    if set(alphabet) == set(string):
        print('YES')
    else:
        print('NO')
