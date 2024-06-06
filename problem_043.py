"""
The number, 1406357289, is a 0 to 9 pandigital number,
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
d_2 d_3 d_4 = 406 is divisible by 2
d_3 d_4 d_5 = 063 is divisible by 3
d_4 d_5 d_6 = 635 is divisible by 5
d_5 d_6 d_7 = 357 is divisible by 7
d_6 d_7 d_8 = 572 is divisible by 11
d_7 d_8 d_9 = 728 is divisible by 13
d_8 d_9 d_10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

string = "0123456789"

p = list(permutations(string))
p = ["".join(x) for x in p] # if x[0] != "0"]

def prime_digits(number: str) -> bool:

    right, limit = 3, 10
    divisors = [2, 3, 5, 7, 11, 13, 17]
    
    while right <= limit:
        digits = number[right - 2 : right + 1]
        print(digits)
        right += 1

    return True

prime_digits("1406357289")