"""
What is the value of the first triangle number to have over five hundred divisors?
"""

divisors = 0
triangle_number = 0
addition = 1
limit = 500

while divisors < limit:
    divisors = 0
    triangle_number += addition
    addition += 1
    for i in range(1, int(triangle_number**0.5) + 1):
        if triangle_number % i == 0:
            divisors += 2

print(triangle_number)