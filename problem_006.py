"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#################################
########## Solution 1 ###########
#################################

def sum_of_squares(n: int) -> int:

    total_sum = 0

    for i in range(1, n + 1):
        total_sum += i**2
    
    return total_sum

def square_of_sum(n: int) -> int:
    """
    Use the fact that the sum of the first n natural numbers is 0.5n(n + 1)
    """

    temp_sum = int(0.5 * n * (n + 1))

    return temp_sum**2

n = 100

answer = square_of_sum(n) - sum_of_squares(n)

print(answer)

#################################
########## Solution 2 ###########
#################################

n = 100

# Use formula for squared numbers
square_sum = n * (2 * n + 1) * (n + 1) / 6
sum_square = n * (n + 1) / 2

answer = int(sum_square**2 - square_sum)

print(answer)