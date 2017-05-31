# You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of
# each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase
# letters should be converted to uppercase. You need to then print the resultant String to output.
#
# Input Format
# The first and only line of input contains the String
# S
# S
#
# Output Format
# Print the resultant String on a single line.
#
# Constraints
# 1 ≤ |S| ≤ 100 where |S| denotes the length of string S.

userInput = input()
result = []
for i in userInput:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())

print(''.join(result))
