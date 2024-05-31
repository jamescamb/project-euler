"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from collections import Counter

def pandigital(multiplicand: int, multiplier: int) -> bool:
    """
    Check if a multiplicand/multiplier/product combination is pandigital
    """

    valid = [str(x) for x in range(1, 10)]
    string = str(multiplicand) + str(multiplier) + str(multiplicand*multiplier)
    
    if "0" in string:
        return False

    dic = Counter(string)
    for num in valid:
        if num not in string or dic[num] > 1:
            return False
    
    return True

def repeat(number: int) -> bool:
    """
    Check if a single number has any repeat/non-valid digits
    """

    if "0" in str(number):
        return False
    
    dic = Counter(str(number))
    for value in dic.values():
        if value > 1:
            return False
    
    return True

lower_limit = 2
upper_limit = 2000

valid_values = [x for x in range(lower_limit, upper_limit) if repeat(x)]
n = len(valid_values)

pandigital_set = set()

for i in valid_values[0: int(n/2)]:
    for j in valid_values:
        if pandigital(i, j):
            pandigital_set.add(i*j)

answer = sum(pandigital_set)
print(answer)