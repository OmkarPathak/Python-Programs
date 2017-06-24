# Today, Monk went for a walk in a garden. There are many trees in the garden and each tree has an English alphabet on
# it. While Monk was walking, he noticed that all trees with vowels on it are not in good state. He decided to take care
# of them. So, he asked you to tell him the count of such trees in the garden.
# Note : The following letters are vowels: 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o' and 'u'.
#
# Input:
# The first line consists of an integer T denoting the number of test cases.
# Each test case consists of only one string, each character of string denoting the alphabet (may be lowercase or
# uppercase) on a tree in the garden.
#
# Output:
# For each test case, print the count in a new line.
#
# Constraints:
# 1≤T≤10
# 1≤length of string≤105
#
# SAMPLE INPUT
# 2
# nBBZLaosnm
# JHkIsnZtTL
#
# SAMPLE OUTPUT
# 2
# 1
#
# Explanation
# In test case 1, a and o are the only vowels. So, count=2

for _ in range(int(input())):
    count  = 0
    string = input().lower()
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    print(count)
