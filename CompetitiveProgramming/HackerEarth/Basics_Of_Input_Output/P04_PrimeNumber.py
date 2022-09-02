# You are given an integer N. You need to print the series of all prime numbers till N.
#
# Input Format
#
# The first and only line of the input contains a single integer N denoting the number till where you need to find the
# series of prime number.
#
# Output Format
#
# Print the desired output in single line separated by spaces.
#
# Constraints
# 1 <= N <=1000

# import math
while(1):
    userInput = int(input("Enter a number until which you want to print prime numbers : "))
    if userInput == 0 or userInput == 1:
        print("Zero and One are not Prime Numbers")
    else:
        for i in range(userInput+1):
            if i == 0 or i == 1:
                continue
            count = 0
            for j in range(1,i+1):
                if i%j == 0:
                    count+=1
            if count<3:
                print(i,end = ' ')
    choice = input("\nDo you want to print more prime numbers? Y or N\n")
    if choice == 'N' or choice == 'n':
        break
# if userInput > 2:
#     print("2",end = ' ')
# for i in range(3, userInput + 2):
#     check = 0
#     for j in range(2, int(math.sqrt(i))+ 1):
#         if i % j == 0:
#             check = 1
#             break
#     if check == 0:
#         print(i, end = ' ')
