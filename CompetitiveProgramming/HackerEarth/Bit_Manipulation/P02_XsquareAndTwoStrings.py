# Xsquare loves to play with strings a lot. Today, he has two strings S1 and S2 both consisting of lower case
# alphabets. Xsquare listed all subsequences of string S1 on a paper and all subsequences of string S2 on a
# separate paper. Xsquare wants to know whether there exists a string which is listed on both the papers.
#
# Xsquare thinks that this task is pretty boring and handed it to you. Please accomplish this task on his
# behalf.
#
# Input
#
# First line of input contains a single integer T denoting the number of test cases. Each test case consists of
# two lines. First line of each test case contains a string denoting string S1. Next line of each test case
# contains a string denoting string S2.
#
# Output
#
# For each test case, Print Yes if both papers contain a common string otherwise Print No.
#
# Constraints
#
# 1 ≤ T ≤ 105
#
# 1 ≤ |S1| ≤ 105
#
# 1 ≤ |S2| ≤ 105
#
# Sum of |S1| over all test case does not exceed 5*105
#
# Sum of |S2| over all test case does not exceed 5*105
#
# Subtasks
#
# Subtask1 : sum of |S1|,|S2| over all test cases does not exceed 103 (25 pts)
# Subtask2 : sum of |S1|,|S2| over all test cases does not exceed 104 (25 pts)
# Subtask3 : sum of |S1|,|S2| over all test cases does not exceed 5*105 (50 pts)
#
# SAMPLE INPUT
# 2
# phackerekarthj
# jhakckerearthp
# hello
# buy
#
# SAMPLE OUTPUT
# Yes
# No
#
# Explanation
# Testcase 1 : There is a common subsequence of letters between S1 and S2. For ex: "hackerearth" is
# subsequence of S1 and S2 both. Testcase 2 : There is no common subsequence of letters between S1 and S2.

testCases = int(input())
for _ in range(testCases):
    string1 = input()
    string2 = input()
    count = 0
    for i in string1:
        if i in string2:
            count += 1

    if count == 0:
        print('No')
    else:
        print('Yes')
