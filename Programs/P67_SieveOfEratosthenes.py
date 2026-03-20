# Sieve of Eratosthenes (Annotated Version)

def sieve(n):
    # ❌ VIOLATION: No input validation
    if n < 2:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            # ❌ VIOLATION: Original started from 2*p (inefficient)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]


if __name__ == '__main__':
    print(sieve(50))
