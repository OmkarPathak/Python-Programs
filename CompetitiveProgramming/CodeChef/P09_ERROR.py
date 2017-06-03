# Lots of geeky customers visit our chef's restaurant everyday. So, when asked to fill the feedback form,
# these customers represent the feedback using a binary string (i.e a string that contains only characters '0'
# and '1'.
#
# Now since chef is not that great in deciphering binary strings, he has decided the following criteria
# to classify the feedback as Good or Bad :
#
# If the string contains the substring "010" or "101", then the feedback is Good, else it is Bad. Note that,
# to be Good it is not necessary to have both of them as substring.
#
# So given some binary strings, you need to output whether according to the chef, the strings are Good or Bad.
#
# Input
# The first line contains an integer T denoting the number of feedbacks. Each of the next T lines contains a
# string composed of only '0' and '1'.
#
# Output
# For every test case, print in a single line Good or Bad as per the Chef's method of classification.
#
# Constraints
# 1 ≤ T ≤ 100
# 1 ≤ |S| ≤ 105
#
# Sum of length of all strings in one test file will not exceed 6*106.
#
# Example
# Input:
# 2
# 11111110
# 10101010101010
#
# Output:
# Bad
# Good

testCases = int(input())
while testCases:
    testCases -= 1
    string = input()
    if '010' in string or '101' in string:
        print('Good')
    else:
        print('Bad')
