"""
What is the 10001st prime number?
"""

limit = 10001
primes = [2, 3]
number = 5

while len(primes) < limit:
    if not 0 in [number % x for x in primes]:
        primes.append(number)
    # Since all primes (other than 2) are odd, we can go up in twos 
    number += 2

print(primes[-1])