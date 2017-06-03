# Fredo is playing a game. The rules of the game are:
# Initially, you are given A units of ammo. There are N obstacles placed on a path. When you hit an obstacle, you gain
# three units ammo and lose one unit of ammo. When you don't hit an obstacle, you lose one unit ammo. If at any instance,
# you are left with 0 ammo units, the game ends there.
#
# Fredo has an array Arr containing N elements corresponding to the N obstacles. If Fredo will hit obstacle i , then Arr[i]=1
# else Arr[i]=0. Fredo asks you to tell him if he will be able to reach the end of the path. If yes, then also tell him
# the remaining number of ammo units. If he is not able to reach the end of the path, tell him the obstacle index at which
# his game would end.
#
# Note: If Fredo reaches the last obstacle, he is said to reach the end of the path.
#
# Input Format:
# The first line consists of an integer T , denoting the number of test cases.
# Each test cases consists of two lines:
# The first line consists of two integers A and N, denoting the initial ammo units Fredo has and the number of obstacles
# respectively. The second line consists of array Arr as described in the question.
#
# Output Format:
# For each test case:
# If he is able to reach the end of the path, print Yes followed by the number of ammo units remaining.
# Else print No followed by the index (1 based) of the obstacle at which the game ends.
#
# Input Constraints:
# 1≤T≤10
# 1≤A≤105
# 1≤N≤105
#
# SAMPLE INPUT
# 2
# 5 5
# 0 0 1 0 1
# 2 5
# 0 0 1 0 1
#
# SAMPLE OUTPUT
# Yes 6
# No 2
#
# Explanation
# Test case 1:
# Initially he has 5 units of ammo.
# at first obstacle, he is left with 4 units of ammo.(he loses one ammo unit at this obstacle)
# at second obstacle, he is left with 3 units of ammo.
# at third obstacle, he is left with 3+3−1=5 units of ammo.(he gains three and loses one ammo unit)
# at fourth obstacle,he is left with 4 ammo units.
# at fifth obstacle, he is left with 6 ammo units.
# Answer: Yes 6
#
# Test case 2:
# The game ends at obstacle 2 as he is left with 0 ammo units there.

testCases = int(input())
while testCases:
    testCases -= 1
    ammo, obstacle = map(int, input().split())
    obstacleHits = [int(i) for i in input().split()]
    if len(obstacleHits) == obstacle:
        for i in range(len(obstacleHits)):
            if obstacleHits[i] == 0:
                ammo -= 1
            elif obstacleHits[i] == 1:
                ammo += 2
            if ammo == 0:
                print('No', i + 1)
                break
        if ammo != 0:
            print('Yes', ammo)
        else:
            pass
