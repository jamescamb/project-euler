"""
Find the product of the coefficients,
for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with 0.
"""

def is_prime(n: int) -> bool:
    """
    Check if input n is prime or not
    """

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def quadratic(a: int, b: int, n: int) -> int:
    """
    Return quadratic formula
    """

    return n**2 + a*n + b

answer = {}
limit = 1001
prime_set = set()

for i in range(-limit, limit, 1):
    for j in range(-limit, limit, 1):
        n = 0
        isPrime = True
        while isPrime:
            formula = quadratic(i, j, n)
            if formula not in prime_set:
                if is_prime(formula):
                    prime_set.add(formula)
                else:
                    isPrime = False
            n += 1
        answer[n] = [i, j]

coeffs = answer[max(answer)]
product = coeffs[0] * coeffs[1]

print(coeffs, product)