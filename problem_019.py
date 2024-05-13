"""
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

year = 1901
month = 1
day = 1
date = 1
answer = 0

months_28_days = [2]
months_30_days = [4, 6, 9, 11]
months_31_days = [1, 3, 5, 7, 8, 10, 12]

for year in range(1901, 2001):
    for month in range(1, 13):
        day = 1
        if date % 7 == 0:
            answer += 1
        if month in months_30_days:
            day += 30 - 1
            date += 30 - 1
        if month in months_31_days:
            day += 31 - 1
            date += 31 - 1
        if month in months_28_days:
            if year % 4 == 0:
                day += 29 - 1
                date += 29 - 1
            else:
                day += 28 - 1
                date += 28 - 1

print(answer)