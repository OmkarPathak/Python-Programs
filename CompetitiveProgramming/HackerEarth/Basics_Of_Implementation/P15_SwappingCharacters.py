# Your are given a string of length N. You have to follow some rounds of swapping in the string until the below explained
# condition is reached.
#
# In each round the, you have to swap the ith and (i+1)th character , then (i+2)th and (i+3)th character and continue till
# the end of string. In each round , a character from the left will be locked i.e not available for swapping after this
# round , thus after some rounds of swapping , all the characters will be locked at their final position to stop any more
# rounds of swapping .
#
# See the sample explanation for more clarity.
#
# Input
#
# The first line of input contains a T, the number of test case. The first line of each Test case will contain an Integer
# N , denoting the length of the string. The second line of each Test case will contain a string of length N.
#
# Output
#
# For each and every test case, output the string after all positions are locked.
#
# Constraints
#
# 0<T<100
#
# 0<N<10000
#
# SAMPLE INPUT
# 2
# 6
# abcdef
# 3
# abc
#
# SAMPLE OUTPUT
# bdfeca
# bca

# Explanation
# For the first test case , the given string is "abcdef" and all the characters are unlocked.
#
# After First round of swap , the string becomes "badcfe" . Now the leftmost unlocked character is locked i.e the string is
# now "b_adcfe".
#
# After Second round of swap , the string becomes "b_dafce". Now the leftmost unlocked character is locked i.e string is
# now "bd_afce".
#
# After Third round of swap , the string becomes "bdfaec" . Now the leftmost unlocked character is locked i.e the string is
# now "bdf_aec".
#
# After Fourth round of swap , the string becomes "bdfeac" . Now the leftmost unlocked character is locked i.e the string is
# now "bdfe_ac"..
#
# After Fifth round of swap , the string becomes "bdfeca" . Now the leftmost unlocked character is locked i.e the string is
# now "bdfec_a".
#
# In the sixth round no more swap occur as there is only single unlocked character is left.
#
# ** ('-' is the partition , where all the characters to its left are locked characters and all the characters to it right
# are unlocked characters).**
#
# Therefore , we print the string "bdfeca".

testCases = int(input())
for _ in range(testCases):
    n = int(input())
    string = list(input())
    start = 0
    fixChars = []
    fixChars = ''
    while start < n:
        for i in range(start, len(string) - 1, 2):
            string[i], string[i + 1] = string[i + 1], string[i]
        fixChars.append(string[start])
        start += 1

    print(fixChars)
