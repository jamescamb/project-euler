"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

upper_limit = 20

factors = []

for i in range(upper_limit, int(upper_limit/2), -1):
    factors.append(i)

answer = 2520

while sum([answer % x for x in factors]) != 0:
    answer += 2520

print(answer)