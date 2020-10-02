'''
problem--
You are given an array of n integers, ar=[arr[0],arr[1],..,arr[n-1]], and a positive integer, k. Find and print the number of (i,j) pairs where i<j and arr[i]+arr[j] is divisible by k.
For example, ar=[1,2,3,4,5,6] and k=5. Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].
Function Description--
Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.
divisibleSumPairs has the following parameter(s):
n: the integer length of array arr
arr: an array of integers
k: the integer to divide the pair sum by
Input Format--
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of arr[arr[0],arr[1],..,arr[n-1]].
Constraints--
2<=n<=100
1<=k<=100
1<arr[i]<=100
Output Format--
Print the number of (i,j) pairs where i<j and arr[i] + arr[j] is evenly divisible by k.
Sample Input--
6 3
1 3 2 6 1 2
Sample Output--
 5
'''

#code here

#!/bin/python3

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i<j and (ar[i]+ar[j])%k==0:
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
