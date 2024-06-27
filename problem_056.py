"""
Considering natural numbers of the form, a^b, where a,b < 100, what is the maximum digital sum?
"""

answer = max(sum(map(int, str(a**b))) for a in range(1, 100) for b in range(1, 100))

print(answer)