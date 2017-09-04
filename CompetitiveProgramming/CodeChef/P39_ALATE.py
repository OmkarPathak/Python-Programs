# Anmol always comes to class when the class is about to end. Frustrated by this behaviour of Anmol, his
# teacher has given him a special question as his homework. We all know that Anmol is very weak at computer
# science thus he came to you for help. Help Anmol in order to solve the problem.
# You are given an array A of length N(1 indexed). You have to process Q queries of two different types:
# 1 x — print func(x)
# 2 x y— change the value of A[x] to y.
# func(x) is defined as ::
#
# func(x)
# {
# 	sum = 0 ;
# 	for(i=x;i<=N;i+=x)
# 		sum = (sum + A[i]*A[i]) ;
# 	return sum ;
# }
#
# For each query of type 1 print the value of func(x) in a new line.
# Input
# The first line contains a single integer T, the number of test cases.
# Each test case is described as follows :
# The first line contains two numbers N and Q.
# In the next line N space separated numbers denoting the values of the array A.
# Each of the following Q lines contains a query of one of the above mentioned two types.
# Note :: Since the test files are large use scanf/printf for I/O.
#
# Output
# For each test case, For each query of type 1 print the required answer.
#
#
# Since the answer can be very large, output it modulo 1000000007
# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ N ≤ 100000
# 1 ≤ Q ≤ 100000
# 1 ≤ A[i] ≤ 1e9
# 1 ≤ x ≤ N
# 1 ≤ y ≤ 1e9
#
# Subtasks
#
# Subtask #1 (20 points), Time limit : 1 sec
# 1 ≤ T<=10, N<=100
#
#
# Subtask #2 (80 points), Time limit : 1 sec
# 1 ≤ T<=10, N<=100000
#
#
# Example
# Input:
# 1
# 5 3
# 1 2 3 4 5
# 1 1
# 2 2 1
# 1 2
# Output:
# 55
# 17

def func(x):
    sum = 0
    for i in range(x, int(n) + 1, x):
        sum = sum + array[i] * array[i]
    return sum

for _ in range(int(input())):
    n, q = input().split()
    array = [int(i) for i in input().split()]
    array.insert(0, 0)
    for _ in range(int(q)):
        inputs = [int(i) for i in input().split()]
        if len(inputs) == 2:
            print(func(inputs[1]))
        else:
            array[inputs[1]] = inputs[2]
