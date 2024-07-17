"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from itertools import combinations

def is_prime(n: int) -> bool:
    """
    Determine if a number is prime or not
    """

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def concatenate_primes(primes: list) -> bool:

    for i in range(len(primes)):
        for j in range(len(primes)):
            if i != j:
                if not is_prime(int(str(primes[i]) + str(primes[j]))):
                    return False
    
    return True

upper_limit = 1500
primes = [x for x in range(2, upper_limit) if is_prime(x)]
print(len(primes))
subarrays = list(combinations(primes, 5))

for subarray in subarrays:
    if concatenate_primes(subarray):
        print(subarray)
        break