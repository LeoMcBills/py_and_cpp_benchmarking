# Description: Generate prime numbers up to a specified limit using the sieve algorithm.
# Why: This tests the efficiency of memory allocation and iteration loops.

# Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (primes[p] == True):
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit) if primes[p]]

print(sieve_of_eratosthenes(300))