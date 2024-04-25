"""
A palindromic number reads the same both ways.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check_palindrome(n: int) -> bool:
    """
    Two pointer approach
    """
    
    s = str(n)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

answer = 0
max_limit, min_limit = 900, 100

# Double for-loop with some speed-ups:
# (1) Start at 999 and work down to 100
# (2) Only check for i > j to avoid double checking where i*j = j*i
# (3) Don't check palindrome if the number is not even bigger than existing best answer
for i in range(max_limit, min_limit, -1):
    for j in range(i, min_limit, -1):
        if i*j < answer:
            break
        if check_palindrome(i*j):
            answer = i*j
            break

print(answer)