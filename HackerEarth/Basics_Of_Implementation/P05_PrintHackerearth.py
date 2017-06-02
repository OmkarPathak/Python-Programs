# As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some 
# problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will
# be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the
# given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please
# help them.
#
# Input:
# The first line will consists of one integer N denoting the length of string.
# Next line will contain the string Str containing only lower case characters.
#
# Output:
# Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).
#
# Constraints:
# 1 ≤ N ≤ 106
# Each character of string Str will be in range [a,z]

h = 0
a = 0
r = 0
e = 0
c = 0
k = 0
t = 0
slen = int(input())
string = input()
for i in string:
    if i == 'h':
        h += 1
    elif i == 'a':
        a += 1
    elif i == 'r':
        r += 1
    elif i == 'e':
        e += 1
    elif i == 'c':
        c += 1
    elif i == 'k':
        k += 1
    elif i == 't':
        t += 1

h //= 2
e //= 2
a //= 2
r //= 2

result = h
if result > a:
    result = a
if result > r:
    result = r
if result > e:
    result = e
if result > c:
    result = c
if result > k:
    result = k
if result > t:
    result = t

print(result)
