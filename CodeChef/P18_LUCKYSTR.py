# A Little Elephant from the Zoo of Lviv likes lucky strings, i.e., the strings that consist only of the lucky digits 4 and 
# 7.
#
# The Little Elephant has K favorite lucky strings A1, A2, ..., AK. He thinks that the lucky string S is good if either
# |S| ≥ 47 or for some j from 1 to K we have that Aj is a substring of S.
#
# The Little Elephant has found N lucky strings B1, B2, ..., BN under the pillow. Now he wants to know which of them are
# good. Help him and find for each i from 1 to N whether the string Bi is good or not.
#
# Notes.
#
# Let S be some lucky string. Then
# |S| denotes the length of the string S;
# S[i] (1 ≤ i ≤ |S|) denotes the ith character of S (the numeration of characters starts from 1);
# The string T of the length M is called a substring of S if for some k from 0 to |S| - M we have
# T[1] = S[k + 1], T[2] = S[k + 2], ..., T[M] = S[k + M].
# Input
# The first line of the input file contains two integers K and N, the number of favorite lucky strings of the Little
# Elephant and the number of strings he has found under the pillow. Each of the following K lines contains one favorite
# lucky string. Namely, jth line among these K lines contains the string Aj. Each of the following N lines contains one
# lucky string that was found under the pillow. Namely, ith line among these N lines contains the string Bi. The input file
# does not contain any whitespaces.
#
# Output
# For each of the N strings that were found under the pillow print Good if it is good, and Bad otherwise.
#
# Constraints
# 1 ≤ K, N ≤ 50
#
# For each string S in the input file we have 1 ≤ |S| ≤ 50.
#
# Each string in the input file consists only of the lucky digits 4 and 7.
#
# Example
#
# Input:
# 2 4
# 47
# 744
# 7444
# 447
# 7774
# 77777777777777777777777777777777777777777777774
#
# Output:
# Good
# Good
# Bad
# Good


N1, K1 = map(int, input().split())
K = []
for i in range(1, N1 + 1):
    K.append(input())
while K1:
    K1 -= 1
    string = input()
    flag = 0
    for i in range(len(K)):
        if K[i] in string:
            flag = 1
            break
        elif (len(string) >= int(K[i])):
            flag = 1
            break
    if flag == 1:
        print('GOOD')
    else:
        print('BAD')
