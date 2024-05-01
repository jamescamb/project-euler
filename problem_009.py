"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""

bound = 1000

for i in range(3, int(bound/2)):
    for j in range(int(bound/2), i, -1):
        if i**2 + j**2 == (1000 - i - j)**2:
            answer = i * j * (bound - i - j)
            print(answer)
            break
