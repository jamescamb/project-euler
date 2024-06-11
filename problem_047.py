"""
The first two consecutive numbers to have two distinct prime factors are 14 = 2*7 and 15 = 3*5
The first three consecutive numbers to have three distinct prime factors are 644, 645, and 646
Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

def len_prime_factors(n: int) -> int:
    
    candidates = [x for x in [2] if n % x == 0] + [x for x in range(3, n // 2 + 1, 2) if n % x == 0]

    return len([x for x in candidates if is_prime(x)])

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

counter, number = 0, 647
length = 4

while counter < length:
    if len_prime_factors(number) == length:
        counter += 1
    else:
        counter = 0
    number += 1

print(number - length)