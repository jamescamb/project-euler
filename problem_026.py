"""
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part
"""

upper_limit = 1000

def calc_longest_recur_cycle(limit):

    max_len = 0
    max_d = 1

    for d in range(1, limit):
        quotient = {0: 0}
        cur_value = 1
        len_recur = 0

        while cur_value not in quotient:
            len_recur += 1
            quotient[cur_value] = len_recur
            cur_value = (cur_value % d) * 10

        if not cur_value:
            continue

        len_recur -= quotient[cur_value]

        if len_recur > max_len:
            max_len = len_recur
            max_d = d

    return max_d

print(calc_longest_recur_cycle(upper_limit))