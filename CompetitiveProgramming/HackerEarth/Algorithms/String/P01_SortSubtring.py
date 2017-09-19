# Given a string S, and two numbers N, M - arrange the characters of string in between the indexes N
# and M (both inclusive) in descending order. (Indexing starts from 0).
#
# Input Format:
# First line contains T - number of test cases.
# Next T lines contains a string(S) and two numbers(N, M) separated by spaces.
#
# Output Format:
# Print the modified string for each test case in new line.
#
# Constraints:
#
# 1≤T≤1000
# 1≤|S|≤10000 // |S| denotes the length of string.
# 0≤N≤M<|S|
# S∈[a,z]
#
# SAMPLE INPUT
# 3
# hlleo 1 3
# ooneefspd 0 8
# effort 1 4
#
# SAMPLE OUTPUT
# hlleo
# spoonfeed
# erofft

for i in range(int(input())):
    user_input = input()
    user_input = user_input.split()
    to_char = int(user_input[2])
    from_char = int(user_input[1])
    string = user_input[0][from_char:to_char + 1]
    replace = ''.join(sorted(string)[::-1])
    print(user_input[0][:from_char] + replace + user_input[0][to_char + 1:len(user_input[0])])
