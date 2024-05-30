"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# We want abcde = a**5 + b**5 + ... + e**5

valid = []
power = 5

lower_limit = 10**(power - 2)
upper_limit = 10**(power + 1) - 1

for i in range(lower_limit, upper_limit):
    string = str(i)
    temp = 0
    for char in string:
        temp += int(char)**power
    if temp == i:
        valid.append(i)

print(valid)
answer = sum(valid)
print(answer)