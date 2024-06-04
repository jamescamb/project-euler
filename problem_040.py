"""
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression:
d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""

answer = 1
counter = 0
upper_limit = 1000000
indices = [1, 10, 100, 1000, 10000, 100000, 1000000]

for i in range(1, upper_limit + 1):
    for j in range(len(str(i))):
        counter += 1
        if counter in indices:
            answer *= int(str(i)[j])

print(answer)