"""
The n-th term of the sequence of triangle numbers is given by t_n = 1/2 n (n + 1), 
so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...


By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""

with open("words.txt", "r") as file:
   words = file.read().replace('"', "")

words = words.split(",")

summations = [0] * len(words)
for i, word in enumerate(words):
    summations[i] += sum([ord(char) - 64 for char in word])

upper_limit = max(summations)

t_nums = [1]
count = 2
while t_nums[-1] < upper_limit:
    t_nums.append(t_nums[-1] + count)
    count += 1

answer = sum([1 if sums in t_nums else 0 for sums in summations])
print(answer)