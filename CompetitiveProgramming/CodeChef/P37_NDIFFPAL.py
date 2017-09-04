# A palindrome is a string that reads same in both directions: forwards and backwards. For example,
# the strings radar and noon are palindromes, whereas the string chef is not a palindrome as being read
# backwards is becomes equal to fehc, which is not equal to chef.
#
# Let's say that the pair of indices (i, j) denotes a palindrome in some string S iff i ≤ j and the
# substring starting at the i-th character and ending at the j-th character of S is a palindrome.
#
# Given an integer N. Your task is to construct a string S such that there are exactly N different
# pairs (i, j) that denotes a palindrome.
#
# Input
# The first line of the input contains an integer T denoting the number of test cases. The description
# of T test cases follows.
#
# The first line of each test case contains a single integer N denoting the sought number of pairs that
# denote palindrome.
#
# Output
# For each test case, output a single line containing a string S, consisting of lowecase Latin letters,
# and having exactly N distinct palindrome-denoting pairs. If there's a few such strings, output any one.
#
# If such string S doesn't exist, output -1 instead of it.
#
# Constraints
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 104
#
# Example
# Input:
# 3
# 6
# 7
# 2
#
# Output:
# noon
# radar
# ab
#
# Explanation:
# Example case 1. In the string "noon", the pairs that denote a palindrome are (1-indexed): (1, 1), (1, 4), (2, 2), (2, 3), (3, 3), (4, 4).
#
# Example case 2. In the string "radar", the pairs that denote a palindrome are (1-indexed): (1, 1), (1, 5), (2, 2), (2, 4), (3, 3), (4, 4), (5, 5).
#
# Example case 3. In the string "ab", the pairs denoting a palindrome are : (1, 1), (2, 2)

for _ in range(int(input())):
    n = int(input())
    s = 'abcdefghijklmnopqrstuvwxyz'
    if (n <= 26):
        print(s[:n])
    else:
        a = n // 26
        b = n % 26
        c = a * s
        c = c + s[:b]
        print (c)
