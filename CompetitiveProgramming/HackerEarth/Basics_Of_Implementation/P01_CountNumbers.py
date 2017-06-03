# Your task is pretty simple , given a string S , find the total count of numbers present in the digit.
#
# Input
#
# The first line contains T , the number of test cases. The first line of each and every testc ase will contain a integer N ,
# the length of the string . The second line of each and every test case will contain a string S of length N.
#
# Output
#
# For each and every testcase , output the total count of numbers present in the string.
#
# Constraints
#
# 0 < T < 200
#
# 0 < N < 10000
#
# SAMPLE INPUT
# 1
# 26
# sadw96aeafae4awdw2wd100awd
#
# SAMPLE OUTPUT
# 4

testCases = int(input())
while testCases:
    testCases -= 1
    N = int(input())
    count = 0
    result = 0
    string = input()
    for i in string:
        if i.isdigit():
            count += 1
        else:
            if count >= 1:
                result += 1
                count = 0

    print(result)
