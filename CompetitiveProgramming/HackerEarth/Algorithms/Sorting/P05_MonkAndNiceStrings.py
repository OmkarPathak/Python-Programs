# Insertion Sort Problem
#
# Monk's best friend Micro's birthday is coming up. Micro likes Nice Strings very much, so Monk decided to gift
# him one. Monk is having N nice strings, so he'll choose one from those. But before he selects one, he need
# to know the Niceness value of all of those. Strings are arranged in an array A, and the Niceness value of
# string at position i is defined as the number of strings having position less than i which are lexicographicaly smaller than
# A[i]. Since nowadays, Monk is very busy with the Code Monk Series, he asked for your help.
# Note: Array's index starts from 1.
#
# Input:
# First line consists of a single integer denoting N. N lines follow each containing a string made of lower case English alphabets.
#
# Output:
# Print N lines, each containing an integer, where the integer in ith line denotes Niceness value of string A[i].
#
# Constraints:
# 1≤N≤1000
# 1≤|A[i]|≤10 ∀ i where 1≤i≤N, where
# |A[i]| denotes the length of
# ith string.
#
# SAMPLE INPUT
# 4
# a
# c
# d
# b
#
# SAMPLE OUTPUT
# 0
# 1
# 2
# 1
#
# Explanation
# Number of strings having index less than 1 which are less than "a" = 0
# Number of strings having index less than 2 which are less than "c": ("a") = 1
# Number of strings having index less than 3 which are less than "d": ("a", "c") = 2
# Number of strings having index less than 4 which are less than "b": ("a") = 1

# My solution
array = []
for i in range(int(input())):
    array.append(input())

for i in range(len(array)):
    count = 0
    for j in range(0, i + 1):
        if array[j] < array[i]:
            count += 1
    print(count)

# Better solution
n = int(input())
a = []
for i in range(n):
    a.append(input())
    ans = 0
    for j in a:
        if j < a[i]:
            ans += 1
    print(ans)
