# Given two strings of equal length, you have to tell whether they both strings are identical.

# Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

# Input :

# First line, contains an intger 'T' denoting no. of test cases.
# Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
# Output:

# For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.
# Constraints:

# 1<= T <=100
# 1<= |S1| = |S2| <= 10^5
# String is made up of lower case letters only.

st1="hello"
str2="ollehll"
stl1=sorted(st1)
stl2=sorted(str2)
flag=0
if len(st1)==len(str2):
    for i in range(len(stl1)):
        if(stl1[i]==stl2[i]):
            flag=1
        else:
            flag=0
            break
if flag==1:
    print("yes")
else:
    print("no")