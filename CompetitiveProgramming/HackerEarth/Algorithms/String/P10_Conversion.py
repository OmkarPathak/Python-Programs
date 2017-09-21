# Given a string, convert it into its number form .
#
# A or a -> 1
# B or b -> 2
# C or c -> 3
# . . .
# Z or z -> 26
# space -> $
# Input:
#
# test cases, t
# string , s
# Output:
#
# Desired O/p
#
# Constraints: string length <=200
#
# SAMPLE INPUT
# 2
# AMbuj verma
# Aaaa bBBB
#
# SAMPLE OUTPUT
# 11322110$22518131
# 1111$2222

for _ in range(int(input())):
    string = input()
    check = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in range(len(string)):
        if string[i].lower() != ' ':
            result.append(check.find(string[i].lower()) + 1)
        else:
            result.append('$')

    print(''.join([str(i) for i in result]))
