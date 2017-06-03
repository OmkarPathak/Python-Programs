# The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the ancient plays are tragedies.
# Therefore the dramatic advisor of ACM has decided to transfigure some tragedies into comedies. Obviously, this work is
# very hard because the basic sense of the play must be kept intact, although all the things change to their opposites. For
# example the numbers: if any number appears in the tragedy, it must be converted to its reversed form before being
# accepted into the comedy play.
#
# Reversed number is a number written in arabic numerals but the order of digits is reversed. The first digit becomes last
# and vice versa. For example, if the main hero had 1245 strawberries in the tragedy, he has 5421 of them now. Note that
# all the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200
# gives 21). Also note that the reversed number never has any trailing zeros.
#
# ACM needs to calculate with reversed numbers. Your task is to add two reversed numbers and output their reversed sum. Of
# course, the result is not unique because any particular number is a reversed form of several numbers (e.g. 21 could be
# 12, 120 or 1200 before reversing). Thus we must assume that no zeros were lost by reversing (e.g. assume that the
# original number was 12).
#
# Input
#
# The input consists of N cases (equal to about 10000). The first line of the input contains only positive integer N. Then
# follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the
# reversed numbers you are to add.
#
# Output
#
# For each case, print exactly one line containing only one integer - the reversed sum of two reversed numbers. Omit any
# leading zeros in the output.
#
# Example
#
# Sample input:
#
# 3
# 24 1
# 4358 754
# 305 794
#
# Sample output:
#
# 34
# 1998
# 1

testCases = int(input())
for i in range(testCases):
    number1, number2 = map(list, input().split())
    result = 0
    result = int(''.join(number1[::-1])) + int(''.join(number2[::-1]))
    result = list(str(result))
    print(int(''.join(result[::-1])))
