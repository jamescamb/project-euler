"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which,
by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

from typing import Tuple
from collections import defaultdict

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def permutations(n: int) -> Tuple[dict, dict]:

    digits = len(str(n))
    perms = defaultdict(list)
    primes = defaultdict(int)

    for i in range(digits):
        for k in range(9):
            new_n = ""
            for j in range(digits):
                if j != i:
                    new_n += str(n)[j]
                else:
                    new_n += str(k)
            if len(str(int(new_n))) == digits:
                perms[i + 1].append(int(new_n))
                primes[i + 1] += 1 if is_prime(int(new_n)) else 0
    
    return perms, primes

def candidates(lower_bound: int, upper_bound: int) -> int:

    cands = defaultdict(int)

    for i in range(lower_bound, upper_bound):
        perms, primes = permutations(i)
        cands[max(primes, key=primes.get())] = min(perms[max(primes, key=primes.get)])
    
    print(cands)

    return max(cands)

answer = candidates(10000, 100000)
print(answer)