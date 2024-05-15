"""
Find the sum of the digits in the number 100!
"""

import math

number = str(math.factorial(100))

answer = 0

for char in number:
    answer += int(char)

print(answer)