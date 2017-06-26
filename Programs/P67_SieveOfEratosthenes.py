# Auhtor: OMKAR PATHAK

# Sieve of Eratosthenes is one of the efficient algorithms to find all the prime numbers upto n, where n can be
# upto 10 million. This algorithm is very efficient and fast and hence is preferred by many competitive programmers.

# Algo:
# 1. Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
# 2. Initially, let p equal 2, the first prime number.
# 3. Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list.
#    These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
# 4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise,
#    let p now equal this number (which is the next prime), and repeat from step 3.
# When the algorithm terminates, all the numbers in the list that are not marked are prime.

def SieveOfEratosthenes(n):
    primes = [True] * (n + 1)
    p = 2                   # because p is the smallest prime

    while(p * p <= n):
        # if p is not marked as False, this it is a prime
        if(primes[p]) == True:
            # mark all the multiples of number as False
            for i in range(p * 2, n + 1, p):
                primes[i] = False

        p += 1
        
    # printing all primes
    for i in range(2, n):
        if primes[i]:
            print(i)

if __name__ == '__main__':
    SieveOfEratosthenes(1000)
