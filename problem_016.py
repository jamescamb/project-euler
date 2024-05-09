"""
What is the sum of the digits of the number 2^1000?
"""

number = 2**1000

answer = 0

for char in str(number):
    answer += int(char)

print(answer)