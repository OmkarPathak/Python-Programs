# Monk introduces the concept of palindrome saying,"A palindrome is a sequence of characters which reads the s
# ame backward or forward."
# Now, since he loves things to be binary, he asks you to find whether the given string is palindrome or not.
# If a given string is palindrome, you need to state that it is even palindrome (palindrome with even length)
# or odd palindrome (palindrome with odd length).
#
# Input:
# The first line consists of T, denoting the number of test cases.
# Next follow T lines, each line consisting of a string of lowercase English alphabets.
#
# Output:
# For each string , you need to find whether it is palindrome or not.
# If it is not a palindrome, print NO.
# If it is a palindrome, print YES followed by a space; then print EVEN it is an even palindrome
# else print ODD.
# Output for each string should be in a separate line.
# See the sample output for clarification.
#
# Constraints:
# 1≤T≤50
# 1≤length of string≤105
#
# SAMPLE INPUT
# 3
# abc
# abba
# aba
#
# SAMPLE OUTPUT
# NO
# YES EVEN
# YES ODD

for _ in range(int(input())):
    user_input = input()
    if user_input == user_input[::-1]:
        if len(user_input) % 2 == 0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')
