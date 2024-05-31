"""
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9's.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

import math

# We are looking for ab/cb == a/c

hash_map = {}
for i in range(10, 100):
    hash_map[i] = []
    for j in range(i, 100):
        if i != j and i % 10 != 0 and j % 10 != 0 and (str(i)[0] in str(j) or str(i)[1] in str(j)):
            hash_map[i].append(j)

valid = []

for num in hash_map:
    for den in hash_map[num]:
        new_num = str(num)[0] if str(num)[1] in str(den) else str(num)[1]
        new_den = str(den)[0] if str(den)[1] in str(num) else str(den)[1]
        if num/den == int(new_num) / int(new_den):
            valid.append([int(new_num), int(new_den)])

num = den = 1
for i, j in valid:
    num *= i
    den *= j

answer = int(den / math.gcd(num, den))
print(answer)