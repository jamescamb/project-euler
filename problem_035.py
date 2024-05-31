"""
The number, 197, is called a circular prime,
because all rotations of the digits: 197, 971, and 719, are themselves prime.
How many circular primes are there below one million?
"""

lower_limit = 2
upper_limit = 1000000

answer = 0

def is_prime(number: int) -> bool:

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

def roll(number: int) -> int:

    string = str(number)
    string += string[0]

    return int(string[1:])

primes = [x for x in range(lower_limit, upper_limit) if is_prime(x) and "0" not in str(x)]

for prime in primes:
    circular = True
    original_prime = prime
    for _ in range(len(str(prime)) - 1):
            prime = roll(prime)
            if not is_prime(prime):
                 circular = False
                 break
    if circular:
         answer += 1

print(answer)