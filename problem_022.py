"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

What is the total of all the name scores in the file?
"""

with open('names.txt', 'r') as file:
    data = file.read()
    names = data.split(',')

names.sort()

name_values = []

for name in names:
    # Account for alphanumeric value of two ord('"')
    temp_value = 60
    for char in name:
        # Offset value so A = 1, B = 2, etc.
        temp_value += ord(char) - 64
    name_values.append(temp_value)

answer = 0

for i, name_value in enumerate(name_values):
    answer += (i + 1) * name_value

print(answer)