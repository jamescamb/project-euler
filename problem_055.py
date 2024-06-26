"""
How many Lychrel numbers are there below ten-thousand?
"""

def is_palindrome(number: str) -> bool:

    left, right = 0, len(number) - 1

    while left < right:
        if number[left] != number[right]:
            return False
        left += 1
        right -= 1
    
    return True

def produce_palindrome(number: int, count: int):

    if is_palindrome(str(number)) and count != 0:
        return count
    elif count >= 50:
        return -1
    else:
        return produce_palindrome(number + int(str(number)[::-1]), count + 1)

answer = 0

for i in range(1, 10000):
    if produce_palindrome(i, 0) == -1:
        answer += 1

print(answer)