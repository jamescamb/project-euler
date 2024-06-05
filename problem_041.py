"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def is_pandigital(n: str) -> bool:

    if "0" in n:
        return False

    for i in range(1, len(n) + 1):
        if str(i) not in n:
            return False
    
    return True

lower_limit = 4231
upper_limit = 10000000

results = [x for x in range(lower_limit, upper_limit, 2) if is_prime(x) and is_pandigital(str(x))]
answer = results[-1]
print(answer)