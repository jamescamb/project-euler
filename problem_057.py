"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

# f_n = p/q, then f_(n + 1) = (p + 2q)/(p + q)

p, q = 1, 1

answer = 0

for i in range(1000):
    a, b = p + 2*q, p + q
    if len(str(a)) > len(str(b)):
        answer += 1
    p, q = a, b

print(answer)