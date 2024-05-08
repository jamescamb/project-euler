"""
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


starting_number = 13

def chain(number):

    print(number)

    if number == 1:
        return
    elif number % 2 == 0:
        return chain(int(number / 2))
    else:
        return chain(3*number + 1)

chain(starting_number)