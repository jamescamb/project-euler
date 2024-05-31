"""
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
"""

def truncate(number: int) -> list:

    numbers = []

    for i in range(1, len(str(number))):
        numbers.append(int(str(number)[0 : i]))
        numbers.append(int(str(number)[i : ]))
    
    return numbers

def is_prime(number: int) -> bool:

    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

answer = 0
lower_limit = 10
upper_limit = 1000000

primes = [x for x in range(lower_limit, upper_limit) if is_prime(x)]

for prime in primes:
    if False not in [is_prime(x) for x in truncate(prime)]:
        answer += prime

print(answer)