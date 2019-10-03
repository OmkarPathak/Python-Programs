# A project was going on related to image processing and to perform experiments and get desired result the image needs to be converted to 
# Gray-Scale using a parameter 'x' and the function P(x) represented the Gray-Code and calculated via x xor (x div 2) where xor stands for 
# bitwise exclusive OR (bitwise modulo 2 addition), and div means integer division.

# It is interesting to note that function P(x) is invertible, which means it is always possible to uniquely restore x given the value of 
# P(x).

# So the group working on the project forgot to keep the original data related to parameter 'x'. Write a program to restore number x from 
# the given value of P(x).

# INPUT:
# The input file contains an integer number y, the value of G(x).

# OUTPUT:
# The output file should contain a single integer x such that G(x) = y.

# CONSTRAINTS:
# 0 ≤ x,P(x) ≤ .

# SAMPLE INPUT 
# 15
# SAMPLE OUTPUT 
# 10

a=int(input())
a=bin(a).replace("0b","")
c=[int(i) for i in str(a)] 
d=[]
e=c[0]
for i in range(0,len(a)):
    if(i==0):
        d.append(c[i])
    else:
        f=c[i]^e
        d.append(f)
        e=f
e=1
g=0
for i in range(0,len(a)):
    g=g+d[len(a)-i-1]*e
    e=e*2
print(g) 
