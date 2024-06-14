"""
The prime 41 can be written as the sume of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def is_prime(n: int) -> bool:

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

upper_bound = 1000000

primes = [2]
i = 3
while sum(primes) < upper_bound:
    if is_prime(i):
        primes.append(i)
    i += 2
    
final_seq = []
right = len(primes)

while right != 0:
    left = 0
    while left + right < len(primes) + 1:
        seq = primes[left : left + right]
        if sum(seq) <= upper_bound:
            if is_prime(sum(seq)):
                if len(seq) > len(final_seq):
                    final_seq = seq
        left += 1
    right -= 1

print(len(final_seq), sum(final_seq))