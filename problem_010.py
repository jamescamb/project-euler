"""
Find the sum of all the primes below two million.
"""

primes = []

limit = 2000000

sieve = set(range(2, limit + 1))
while sieve:
    prime = min(sieve)
    primes.append(prime)
    sieve -= set(range(prime, limit + 1, prime))

answer = sum(primes)

print(answer)