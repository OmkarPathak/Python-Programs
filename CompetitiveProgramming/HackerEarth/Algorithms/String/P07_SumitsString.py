# Given a string 'S' , u need to tell whether it is 'sumit's string or not'.
#
# A string is called 'Sumit's String' , if distance between adjacent character is 1.
#
# Consider that the alphabets are arranged in cyclic manner from 'a' to 'z'. distance between any character
# 'x' and 'y' will be defined as minimum number of steps it takes 'x' to reach 'y'. Here, character 'x' can
# start moving clockwise or anti-clockwise in order to reach at position where character 'y' is placed.
#
# Print 'YES' if it is Sumit's string else print 'NO', for each yest case.
#
# Input :
#
# test cases, t
# string , s
# Output:
#
# Desired O/p
#
# Constraints :
#
# string length<=250
# string has only lower case letters
#
# SAMPLE INPUT
# 3
# aba
# zza
# bcd
#
# SAMPLE OUTPUT
# YES
# NO
# YES

for _ in range(int(input())):
    string = input()
    sumit_string = True
    check = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(string) - 1):
        check_first = check.find(string[i]) + 1
        check_second = check.find(string[i + 1]) + 1
        if abs(check_second - check_first) == 1 or abs(check_second - check_first) == 25:
            continue
        else:
            sumit_string = False
            break

    if sumit_string:
        print('YES')
    else:
        print('NO')
