def main():
    t = int(input())
    res = [2,3,1]
    last = 3
    check = 4
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(1)
        elif (n & (n-1)) == 0:
            print(-1)
        elif n <= last:
            for i in range(n):
                print(res[i], end=" ")
            print()
        else:
            for i in range(last):
                print(res[i], end=" ")
            last += 1
            while last <= n:
                if last == check:
                    res.append(last + 1)
                    res.append(last)
                    print((last + 1), end=" ")
                    print(last, end=" ")
                    last += 2
                    check *= 2
                else:
                    print(last, end=" ")
                    res.append(last)
                    last += 1
            print()
            last -= 1
    return 0

main()
