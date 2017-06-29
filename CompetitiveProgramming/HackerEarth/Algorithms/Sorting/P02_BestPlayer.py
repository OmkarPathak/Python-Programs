# Bubble Sort Problem

# It's Lolympics 2016 right now, and we all know who's the best player there right now: Kalyani! Obviously, he has a
# huge female fan following and he has to make sure they are all happy and rooting for him to win the gold medals.
#
# But with fan following comes arrogance and lack of time. Thus, he has sufficient time to interact with atmost T of
# his fans. Each fan is defined by two parameters : Name and Fan Quotient. The name defines the name of the fan, while
# the fan quotient is a measure of the fan's devotion towards Kalyani. Higher the fan quotient, greater is the devotion.
# Kalyani now wants to meet T of his fans. While selecting the fans he wants to meet, he wants to make sure that a fan
# with a higher fan quotient should be given a chance in favour of those with lesser fan quotient. In case of ties, he
# sorts their name lexicographically and chooses the lexicographically lesser named fan.
#
# Given details of N fans, can you help out Kalyani by giving him a list of fans he would be interacting with?
#
# Input Format :
#
# The first line contains N and T, the number of fans and the maximum number of fans Kalyani can meet. Each of the
# next N lines contains a string and an integer separated by a space. The string denotes the name of the fan while the
# integer depicts the fan quotient.
#
# Output Format :
#
# Output T lines, each containing the name of the fans selected. Fans with higher fan quotient should be outputted
# first and in case of a tie, the lexicographically minimum name should come first.
#
# Constraints :
# 1≤T≤N≤1000
# 1≤lengthofname≤20
# 1≤fanquotient≤109
#
# Name would only consist of characters in set [a-z]. It is not guaranteed that the names are distinct.
#
# SAMPLE INPUT
# 3 2
# surbhi 3
# surpanakha 3
# shreya 5
#
# SAMPLE OUTPUT
# shreya
# surbhi

# less efficient solution
n, t = map(int, input().split())
fans = []
for _ in range(n):
  fans.append(input().split())

for i in range(n - 1, 0, -1):
  for j in range(i):
    if int(fans[j][1]) > int(fans[j + 1][1]):
      fans[j], fans[j + 1] = fans[j + 1], fans[j]

fans = fans[::-1]

for i in range(t):
  if int(fans[i][1]) == int(fans[i + 1][1]):
    check = [fans[i][0], fans[i + 1][0]]
    check.sort()
    print(check[0])
  else:
    print(fans[i][0])

# more efficient solution
n,m = map(int,input().split())
s={}
for i in range(n):
    k,v=input().split()
    v=int(v)
    if v not in s:
        s[v]=[k]
    else:
        s[v].append(k)
        s[v].sort()
list1=[x for x in s.keys()]
list1.sort(reverse=True)
c=0
for i in list1:
    if len(s[i])>0:
        for j in s[i]:
            print (j)
            c=c+1
            if c == m:
                break
    if c==m:
        break
