# Manna is extremely disappointed to find out that no one in his college knows his first name. Even his classmates call
# him only by his last name. Frustrated, he decides to make his fellow college students know his first name by forcing
# them to solve this question.
#
# You are given a long string as input in each testcase, containing any ASCII character. Your task is to find out the
# number of times SUVO and SUVOJIT appears in it.
#
# Note: This problem must be solved in C language only.
#
# Input Format
# The first line contains the number of testcases, T. Next, T lines follow each containing a long string S.
#
# Output Format
# For each long string S, display the no. of times SUVO and SUVOJIT appears in it.
#
# Constraints
#
# 1 <= T <= 100
# 1 <= Length of each string <= 150
#
# SAMPLE INPUT
# 3
# SUVOJITSU
# 651SUVOMN
# $$$$$SUVOSUVOJIT$$$$$
#
# SAMPLE OUTPUT
# SUVO = 0, SUVOJIT = 1
# SUVO = 1, SUVOJIT = 0
# SUVO = 1, SUVOJIT = 1

testCases = int(input())
for _ in range(testCases):
    suvojit = 0
    suvo = 0
    s = input()
    suvojit = s.count("SUVOJIT")
    suvo = s.count("SUVO")
    print('SUVO = ',suvo-suvojit,', SUVOJIT = ',suvojit,sep='')
