from collections import defaultdict


IN = open("in.txt").read().splitlines()
items = IN[0].split(",")


def get_hash(string):
    val = 0
    for char in string:
        ascii_value = ord(char)
        val += ascii_value
        val *= 17
        val %= 256
    return val


boxes = defaultdict(dict)
for item in items:
    if "=" in item:
        label, value = item.split("=")
        hashed = get_hash(label)
        boxes[hashed][label] = value
    if "-" in item:
        label = item.split("-")[0]
        hashed = get_hash(label)
        if label in boxes[hashed]:
            del boxes[hashed][label]

s = 0
for number, box in boxes.items():
    value = 0
    for i, (label, lens) in enumerate(box.items()):
        value += int(lens) * int(number+1) * (i+1)
    s += value

print(s)
