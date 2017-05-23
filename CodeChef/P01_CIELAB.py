# In Ciel's restaurant, a waiter is training. Since the waiter isn't good at arithmetic,
# sometimes he gives guests wrong change. Ciel gives him a simple problem. What is A-B (A minus B) ?
#
# Surprisingly, his answer is wrong. To be more precise, his answer has exactly one wrong digit.
# Can you imagine this? Can you make the same mistake in this problem?
#
# Input
# An input contains 2 integers A and B.
#
# Output
# Print a wrong answer of A-B. Your answer must be a positive integer containing the same number of digits
# as the correct answer, and exactly one digit must differ from the correct answer. Leading zeros are not
# allowed. If there are multiple answers satisfying the above conditions, anyone will do.
#
# Constraints
# 1 ≤ B < A ≤ 10000
#
# Sample Input
# 5858 1234
#
# Sample Output
# 1624
#
# Output details
# The correct answer of 5858-1234 is 4624. So, for instance, 2624, 4324, 4623, 4604 and 4629 will be accepted,
# but 0624, 624, 5858, 4624 and 04624 will be rejected.

# MY SOLUTION:

## This solution gives error in codechef as this consumes more memory

# A, B = input().split()
# result = list(str(int(A) - int(B)))
# result[random.randint(0, 3)] = str(random.randint(0, 9))
# print(int(''.join(result)))

A, B = map(int, input().split())
C = A - B
if C % 10 == 9:
    C = C - 1
else:
    C = C + 1
print(C)

# Output For above solution:
# 5858 1234
# 4625
