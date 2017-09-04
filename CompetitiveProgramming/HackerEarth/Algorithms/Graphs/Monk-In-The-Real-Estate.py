# The Monk wants to buy some cities. To buy two cities, he needs to buy the road connecting those two cities. 
# Now, you are given a list of roads, bought by the Monk. You need to tell how many cities did the Monk buy.
#
# Input:
# First line contains an integer T, denoting the number of test cases. The first line of each test case
# contains an integer E, denoting the number of roads. The next E lines contain two space separated
# integers X and Y, denoting that there is an road between city X and city Y.
#
# Output:
# For each test case, you need to print the number of cities the Monk bought.
#
# Constraint:
# 1 <= T <= 100
# 1 <= E <= 1000
# 1 <= X, Y <= 10000
#
# SAMPLE INPUT
# 1
# 3
# 1 2
# 2 3
# 1 3

for _ in range(int(input())):
    roads = int(input())
    lst = set([])
    for i in range(roads):
        node1,node2 = map(int,input().split())
        lst.add(node1)
        lst.add(node2)
    print(len(lst))
