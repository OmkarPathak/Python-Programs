def sum(x):
    if x < 0:
        return -(-x * (-x + 1) // 2)
    else:
        return x * (x + 1) // 2

while True:
    try:
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if b < 0:
            print(sum(a) - sum(b + 1))
        elif a <= 0:
            print(sum(b) + sum(a))
        else:
            print(sum(b) - sum(a - 1))
    except EOFError:
        exit(0)
