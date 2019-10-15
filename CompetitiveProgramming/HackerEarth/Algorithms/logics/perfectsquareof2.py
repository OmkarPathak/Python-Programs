# Efficient Python program to check entered number is a perfect square of 2 or not
# Example
# 8
# Its a perfect square of 2



n = int(input("Enter a number"))
if n & (n - 1) == 0:
    print("Its a perfect square of 2")
else:
    print("Its not perfect square")
