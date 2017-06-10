# Given A String S Find The Number Of White Spaces In The Given String S.
#
# Input Format
#
# Take Input String S
#
# Output Format
#
# Number Of White Spaces In S
#
# Constraints
#
# 0 < S < 100001
#
# SAMPLE INPUT
# Hello World
#
# SAMPLE OUTPUT
# 1

string = input()
count = 0
for i in string:
    if i != ' ':
        pass
    else:
        count += 1

print(count)
