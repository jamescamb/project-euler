"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

a, b, index = 0, 1, 1

digit_limit = 1000

while len(str(b)) < digit_limit:

    index += 1
    c = a + b
    a = b
    b = c

print(index)