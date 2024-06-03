"""
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c},
there are exactly three solutions for p = 120.
For which value of p <= 1000 is the number of solutions maximised?
"""

p_max = 1000

# p = a + b + c
# a**2 = b**2 + c**2
# a > b, c

answer = max_length = 0

for p in range(120, p_max + 1):
    temp_sum = 0
    for a in range(1, int(p / 2)):
        for b in range(1, p - a):
            c = p - a - b
            temp_sum += 1 if a**2 == b**2 + c**2 else 0
    if temp_sum > max_length:
        answer = p
        max_length = temp_sum

print(answer)