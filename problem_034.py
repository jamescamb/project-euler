"""
145 is a curious number, as 1! + 4! + 5! = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""

import math

# Obtained through trial and error
lower_limit = 144
upper_limit = 40731

answer = 0

for i in range(lower_limit, upper_limit):
    if sum([math.factorial(int(x)) for x in str(i)]) == i:
        answer += i

print(answer)