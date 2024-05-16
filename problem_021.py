"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

Evaluate the sum of all the amicable numbers under 10,000.
"""

upper_limit = 10000

d_function = {}

for i in range(2, upper_limit + 1):
    divisors = [x for x in range(1, int(i/2) + 1) if i % x == 0]
    d_function[i] = sum(divisors)

amicable_numbers = set()

for n, d_n in d_function.items():
    if d_n in d_function and d_function[d_n] == n and n != d_n:
        amicable_numbers.add(n)
        amicable_numbers.add(d_n)

answer = sum(amicable_numbers)

print(answer)