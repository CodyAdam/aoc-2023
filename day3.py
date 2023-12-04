from collections import defaultdict
from functools import reduce
IN = open("in.txt").read().splitlines()

NUM = "1234567890"

grid = {}
H = len(IN)
W = len(IN[0])


for y, line in enumerate(IN):
    print(line)
    current = []
    for x, char in enumerate(line):
        if char not in NUM and len(current):
            current = []
        elif char in NUM:
            current.append(char)
            grid[(x, y)] = current
    if len(current):
        grid[(len(line)-1, y)] = current

print()

print(grid)
def clamp(a, mini, maxi):
    return max(min(a, maxi), mini)


s = 0
stars = defaultdict(list)
for (x, y) in grid:
    cell = grid[(x, y)]
    added = False
    for yy in range(clamp(y-1, 0, W-1), clamp(y+2, 0, W)):
        for xx in range(clamp(x-1, 0, H-1), clamp(x+2, 0, H)):
            val = IN[yy][xx]
            # print(val, end="")
            if not added and val not in NUM and val == "*":
                stars[(xx, yy)].append(cell)

for val in stars.values():
    # remove duplicates by reference
    new_arr =[]
    while len(val):
        v = val.pop()
        if v not in new_arr:
            new_arr.append(v)
    if len(new_arr) == 2:
        s += int("".join(new_arr[0])) * int("".join(new_arr[1]))


print(stars)
print(s)

# 75741499