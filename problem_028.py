"""
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
5 x 5: 1 | 3, 5, 7, 9 | 13, 17, 21, 25 |
       1 | +2         | +4             | +6
6 x 6: 1 | 3, 5, 7, 9 | 13, 17, 21, 25 | 31, 37, 43, 49 |
       1 | +2         | +4             | +6             | +8
"""

sum = 1
number = 1
size = 1001
counter = 0

while number < size*size:
    addition = 2 + 2 * (counter // 4)
    number += addition
    sum += number
    counter += 1

print(sum)