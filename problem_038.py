"""
What is the largest 1 to 9 pandigital 9-digit number
that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""

from collections import Counter

def is_pandigital_combination(number: int, multiplier: int) -> list[bool, int]:

    string = ""
    for i in range(1, multiplier + 1):
        string += str(i*number)
    
    return is_pandigital(string), int(string)

def is_pandigital(string: str) -> bool:

    if "0" in string or len(string) != 9:
        return False
    
    valid = [str(x) for x in range(1, 10)]
    for num in valid:
        if num not in string:
            return False
    
    dic = Counter(string)
    for value in dic.values():
        if value > 1:
            return False
    
    return True

answer = 0

for i in range(1, 10000):
    for j in range(2, 10):
        pandigit, number = is_pandigital_combination(i, j)
        if pandigit:
            print(i, j, number)
            answer = max(answer, number)

print(answer)