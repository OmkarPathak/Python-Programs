# Hihi is the grandfather of all geeks in IIITA. He and his crazy ideas.....Huh..... Currently, hihi is working on his most famous project 
# named 21 Lane, but he is stuck at a tricky segment of his code.

# Hihi wants to assign some random IP addresses to users, but he won't use rand(). He wants to change the current IP of the user's computer 
# to the IP such that its hash is next hash greater than the hash of original IP and differs by only 1 bit from the hash of original IP.

# Smart Hihi already hashed the IP to some integer using his personal hash function. What he wants from you is to convert the given hashed 
# IP to the required IP X as mentioned above.

# OK, just find the find the smallest number greater than n with exactly 1 bit different from n in binary form

# Input :

# First line contains single integer T ( 1 <= T <= 10^6)- number of test cases. Second line contains hashed IP N ( 1 <= N <= 10^18)

# Output :

# Print T lines, each containing an integer X, the required IP.(don't worry Hihi will decode X to obtain final IP address)

# SAMPLE INPUT 
# 5
# 6
# 4
# 10
# 12
# 14
# SAMPLE OUTPUT 
# 7
# 5
# 11
# 13
# 15


for _ in range(int(input())):
    a=int(input())
    print(a|a+1)
