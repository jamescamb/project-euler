"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

hash_map = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
            20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
            1000: "one thousand"}

limit = 1000

answer = 0

def number_to_word(number: int) -> str:
    """
    Returns the word for a number in British English
    Only designed to work up to 1000
    """

    if number in hash_map:
        return hash_map[number]
    elif 20 < number < 100:
        return hash_map[(number // 10) * 10] + "-" + hash_map[number % 10]
    elif 99 < number < 1000:
        and_word = " and " if number % 100 != 0 else ""
        return hash_map[(number // 100)] + "-hundred" + and_word + number_to_word(number - (number // 100)*100)
    else:
        print("Error")
        raise ValueError()

for i in range(limit):
    answer += len(number_to_word(i + 1).replace(" ", "").replace("-", ""))

print(answer)