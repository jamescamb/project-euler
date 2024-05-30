"""
How many different ways can £2 be made using any number of coins?
"""

total = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

possible = [0] * (total + 1)
possible[0] = 1

for coin in coins:
    for i in range(coin, total + 1):
        possible[i] += possible[i - coin]

print(possible[total])