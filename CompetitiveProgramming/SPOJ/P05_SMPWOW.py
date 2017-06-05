# Input
#
# Given a positive integer 0 < x < 50.
#
# Output
#
# Print one word: Wo...ow (letter o must be repeted x times).
#
# Example 1
#
# Input:
# 1
#
# Output:
# Wow
# Example 2
#
# Input:
# 7
#
# Output:
# Wooooooow

check = int(input())
print('W' + check * 'o' + 'w')
