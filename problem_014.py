"""
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def chain(number, known_len):

    if number == 1:
        return 1
    elif number in known_len:
        return known_len[number]
    elif number % 2 == 0:
        return chain(int(number / 2), known_len) + 1
    else:
        return chain(int((3*number + 1) / 2), known_len) + 2

chain_length = 0
starting_number = 0

known_lengths = {}

upper_limit = 1000000

for i in range(int(upper_limit / 2), upper_limit):
    chain_test = chain(i, known_lengths)
    known_lengths[i] = chain_test
    if chain_test > chain_length:
        chain_length = chain_test
        starting_number = i

print(starting_number, "has length", chain_length)