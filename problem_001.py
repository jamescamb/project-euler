"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples = [3, 5]
upper_bound = 1000

answer = 0

for i in range(upper_bound):
    answer += i if 0 in [i % x for x in multiples] else 0

print(answer)