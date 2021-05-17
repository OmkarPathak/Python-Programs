#Given a positive number N, check if the number is a Jumping number or not. 
#A number is defined as a Jumping Number if all adjacent digits in it have an absolute difference of 1. 
#For example 2, 23 and 4343456 are Jumping numbers but 296 and 89498 are not

num = input("Enter a number ")
lst = [int(x) for x in num]
n = len(lst)
res = 1
for ele in range(0,n-1):
    if abs(lst[ele] - lst[ele+1]) != 1:
        res = 0
if res == 1:
    print("JUMPING NUMBER")
else:
    print("NOT A JUMPING NUMBER")
