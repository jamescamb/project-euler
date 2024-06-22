"""
Find the smallest positive integer x,
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def contain_same_digits(arr: list) -> bool:

    sorted_nums = [int("".join(sorted(str(arr[0]))))]

    for i in range(1, len(arr)):
        number = int("".join(sorted(str(arr[i]))))
        if number != sorted_nums[i - 1]:
            return False
        else:
            sorted_nums.append(number)

    return True

for i in range(1, 1000000):
    candidates = [j*i for j in range(1, 7)]
    if contain_same_digits(candidates):
        print(candidates[0])
        break