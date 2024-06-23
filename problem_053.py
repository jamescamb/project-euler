"""
How many, not necessarily distinct, values of n choose r
for 1 <= n <= 100, are greater than one-million?
"""

from math import comb

answer = 0

for n in range(1, 101):
    for k in range(0, n + 1):
        if comb(n, k) > 1000000:
            answer += 1

print(answer)