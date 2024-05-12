"""
Find the maximum total from top to bottom of the triangle
"""

import numpy as np

triangle = np.array([75,
                     95, 64,
                     17, 47, 82,
                     18, 35, 87, 10,
                     20,  4, 82, 47, 65,
                     19,  1, 23, 75,  3, 34,
                     88,  2, 77, 73,  7, 63, 67,
                     99, 65,  4, 28,  6, 16, 70, 92,
                     41, 41, 26, 56, 83, 40, 80, 70, 33,
                     41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
                     53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
                     70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
                     91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
                     63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
                      4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23])

lines = []
n_lines = 16

count = 0

for i in range(n_lines):
    lines.append(i + count)
    count += i

answer = 0

index = 0

# Greedy implementation
for i in range(len(lines) - 1):
    line = triangle[lines[i] : lines[i + 1]]
    line = line[index : index + 2]
    answer += max(line)
    index = np.argmax(line) + index

print(answer)

# Optimised implementation
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def parse_triangle() -> list[list[int]]:
    return [[int(word) for word in line.split()] for line in triangle.strip().split("\n")]

def solution_bottom_up() -> int:
    triangle = parse_triangle()
    for row_i in reversed(range(len(triangle) - 1)):
        row = triangle[row_i]
        for col_i in range(len(row)):
            row[col_i] += max(
                triangle[row_i + 1][col_i], triangle[row_i + 1][col_i + 1]
            )
    return triangle[0][0]

answer = solution_bottom_up()

print(answer)