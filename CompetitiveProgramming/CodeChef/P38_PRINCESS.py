# We all know that the princess is very beautiful but one day jealous from her beauty, a person asked a 
# question from princess in order to check her wisdom. Since princess is not good at programming you need
# to help her in solving the problem.
# You are given a string of length N. You have to check among all the the substrings that whether a substring
# exist or not which is palindrome and having length greater than 1. If such a substring exists then print
# YES else print NO.
#
# Input
# The first line contains a single integer T, the number of test cases. Each test case is described by a
# single line containing a string.
#
# Output
# For each test case, output a single line containing the YES or NO.
#
# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ N ≤ 100000
#
# Example
# Input:
# 2
# ab
# babba
#
# Output:
# NO
# YES
# Explanation
# Example case 1.The only substring whose length is greater than 1 is ab, and its not a palindrome.
#
# Example case 2.abba is a substring of the string and its a palindrome thus YES.

def manacher(string):

    string_with_bounds = '#'.join('^{}$'.format(string))
    length = len(string_with_bounds)
    P = [0] * length
    center = right = 0

    for i in range(1, length - 1):
        P[i] = (right > i) and min(right - i, P[2 * center - i])

        # Attempt to expand palindrome centered at i
        while string_with_bounds[i + 1 + P[i]] == string_with_bounds[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > right:
            center, right = i, i + P[i]

    # Find the maximum element in P and return the string
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return string[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

for _ in range(int(input())):
    string = input()
    result = manacher(string)
    if len(result) > 1:
    	print('YES')
    else:
    	print('NO')
