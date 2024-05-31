"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from collections import Counter

def pandigital(multiplicand: int, multiplier: int, product: int) -> bool:
    """
    Check if a multiplicand/multiplier/product combination is pandigital
    """

    valid = [str(x) for x in range(1, 10)]
    string = str(multiplicand) + str(multiplier) + str(product)

    for char in string:
        if char not in valid:
            return False

    dic = Counter(string)
    for num in valid:
        if num not in string or dic[num] != 1:
            return False
    
    return True

lower_limit = 2
upper_limit = 10000

pandigital_set = set()

for i in range(lower_limit, upper_limit):
    for j in range(i, upper_limit):
        if pandigital(i, j, i*j):
            print(i, j, i*j)
            pandigital_set.add(i*j)

print(pandigital_set)