# You are given container full of water. Container can have limited amount of water. You also have
# N bottles to fill. You need to find the maximum numbers of bottles you can fill.
#
# Input:
# First line contains one integer, T, number of test cases.
# First line of each test case contains two integer, N and X, number of bottles and capacity of the container.
# Second line of each test case contains
# N space separated integers, capacities of bottles.
#
# Output:
# For each test case print the maximum number of bottles you can fill.
#
# Constraints:
# 1≤T≤100
# 1≤N≤104
# 1≤X≤109
#
# SAMPLE INPUT
# 1
# 5 10
# 8 5 4 3 2
#
# SAMPLE OUTPUT
# 3

for _ in range(int(input())):
    N, capacity = map(int, input().split())
    capacities = [int(bottle) for bottle in input().split()]
    capacities.sort()
    check, bottles = 0, 0
    for i in range(len(capacities)):
        if check > capacity:
            bottles -= 1
            break
        bottles += 1
        check += capacities[i]

    print(bottles)
