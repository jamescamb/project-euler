"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis,
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

upper_limit = 28123

test_numbers = [x for x in range(12, upper_limit + 1) if x % 2 == 0 or x % 5 == 0]

abundant_numbers = []

for i in test_numbers:
    divisors_pt1 = [x for x in range(1, int(i**0.5) + 1) if i % x == 0]
    divisors_pt2 = [i//x for x in range(2, int(i**0.5) + 1) if i % x == 0]
    divisors = set(divisors_pt1 + divisors_pt2)
    if sum(divisors) > i:
        abundant_numbers.append(i)

print(len(abundant_numbers))

sums = [0] * (upper_limit + 1)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        two_sum = abundant_numbers[i] + abundant_numbers[j]
        if two_sum <= upper_limit and sums[two_sum] == 0:
            sums[two_sum] = two_sum

answer = sum(range(1, upper_limit + 1)) - sum(sums)

print(answer)