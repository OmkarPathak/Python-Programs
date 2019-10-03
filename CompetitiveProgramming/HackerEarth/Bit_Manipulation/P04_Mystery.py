# In the world of dragon ball, Goku has been the greatest rival of Vegeta. Vegeta wants to surpass goku but never succeeds. Now that he
# knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. He gives certain inputs and 
# outputs , Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge, your task is 
# to find the logic and and help him win the challenge.

# INPUT :

# Given a series of numbers(inputs) and each number(N) on a newline.

# OUTPUT :

# For the given input , Output the required ans.

# NOTE :

# No. of test cases are unknown.

# Use Faster I/O Techniques.

# CONSTRAINTS :

# 0<= N <= 10^18

# SAMPLE INPUT 
# 0
# 1
# 5
# 12
# 22
# 1424
# SAMPLE OUTPUT 
# 0
# 1
# 2
# 2
# 3
# 4

while(1):
    try:
        r=bin(int(input()))
        print(r.count('1'))
    except:
        break
