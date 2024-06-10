"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

# x is odd and not a prime
# p is a prime
# y is any integer
# x = p + 2 * y**2

def is_prime(x: int) -> bool:

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    
    return True

def valid(x: int) -> bool:

    for i in range(x, 1, -2):
        if is_prime(i):
            for j in range(1, int(((x - i)/2)**0.5 + 1)):
                if x == i + 2 * j**2:
                    return True
    
    return False

lower_bound = 33
upper_bound = 10000

for i in range(lower_bound, upper_bound, 2):
    if not is_prime(i) and not valid(i):
        print("answer", i)
        break