"""
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

def is_palindrome(number) -> bool:

    # Two-pointer approach
    left, right = 0, len(str(number)) - 1

    while left < right:
        if str(number)[left] == str(number)[right]:
            left += 1
            right -= 1
        else:
            return False
    
    return True

answer = 0
upper_limit = 1000000

for i in range(upper_limit):
    if is_palindrome(i) and is_palindrome("{0:b}".format(i)):
        answer += i

print(answer)