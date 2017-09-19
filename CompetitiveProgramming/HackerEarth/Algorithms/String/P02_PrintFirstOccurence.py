# Given a string containing only lower case letters ,print first occurrence of all the letters present
#  in that order only.
#
# Input :
#
# Test cases, t
# string ,s
# Output :
#
# Desired Output
#
# Constraint :
#
# string length <=200
#
# SAMPLE INPUT
# 2
# aasdvasvavda
# sajhags
#
# SAMPLE OUTPUT
# asdv
# sajhg
#

for _ in range(int(input())):
    user_input = input()
    string = []
    for i in range(len(user_input)):
        if user_input[i] not in string:
            string.append(user_input[i])

    print(''.join(string))
