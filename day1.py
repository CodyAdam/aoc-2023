import re
s = 0
lines = open("in.txt").read().splitlines()
DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

for line in lines:
    digits = []
    i = 0
    while i < len(line):
        print(line[i:])
        for digit in DIGITS:
            if line[i:].startswith(digit):
                digits.append(DIGITS[digit])
        i += 1

    print(digits)
    s += int(str(digits[0]) + str(digits[-1]))
print(s)
