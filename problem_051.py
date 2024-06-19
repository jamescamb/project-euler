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

import itertools
from collections import defaultdict

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def replace_vals(digits: int) -> list:

    result = list(itertools.product([0, 1], repeat=digits))
    if len(result) > 1:
        return result[1:]
    else:
        return result

def permutations(n: int) -> dict:

    digits = len(str(n))
    perms = defaultdict(list)
    vals = replace_vals(digits)
    count = 0

    for val in vals:
        count += 1
        for k in range(10):
            new_n = ""
            for j in range(digits):
                if val[j] == 0:
                    new_n += str(n)[j]
                else:
                    new_n += str(k)
            if len(str(int(new_n))) == digits and is_prime(int(new_n)):
                perms[count].append(int(new_n))
    
    return perms

def candidates(lower_bound: int, upper_bound: int) -> int:

    cands = defaultdict(int)

    for i in range(lower_bound, upper_bound):
        perms = permutations(i)
        if perms:
            max_len = max(perms, key=lambda k: len(perms[k]))
            length = len(perms[max_len])
            min_prime = min(perms[max_len])
            if not cands[length]:
                cands[length] = min_prime
    
    print(cands)

    return cands[max(cands)]

answer = candidates(10000, 100000)
print(answer)