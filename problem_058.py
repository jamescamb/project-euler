"""
Starting with  and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued,
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

def is_prime(n: int) -> bool:

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# 1: 1
# 2:  3,  5,  7,  9
#   +10,+12,+14,+16
# 3: 13, 17, 21, 25
#   +18,+20,+22,+24
# 4: 31, 37, 43, 49

# 1,  3,  5,  7,  9,  13,  17,  21,  25,  31,  37,  43,  49
# 1, +2, +2, +2, +2,  +4,  +4,  +4,  +4,  +6,  +6,  +6,  +6

corners = [1]
primes, length, side, answer = 0, 1, 1, 0

for i in range(100000*4):
    corners.append(corners[-1] + 2 + 2 * (i // 4))
    if (i + 1) % 4 == 0:
        primes += sum([is_prime(x) for x in corners[-4:]])
        length += 4
        side += 2
        if primes / length < 0.1:
            answer = side
            break

print(answer)