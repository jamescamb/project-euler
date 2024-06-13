"""
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

delta = 3330
lower_bound = 1000
upper_bound = 10000 - 2 * delta

for i in range(lower_bound, upper_bound):
    if is_prime(i):
        a, b, c = (i + j * delta for j in range(3))
        if is_prime(b) and is_prime(c):
            if sorted(str(a)) == sorted(str(b)) == sorted(str(c)):
                print(int(str(a) + str(b) + str(c)))