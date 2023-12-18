from collections import defaultdict
IN = open("in.txt").read().splitlines()
DIRS = {
    "0": (1, 0),
    "2": (-1, 0),
    "3": (0, -1),
    "1": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

# PARSE
current = (0, 0)
points = [current]
for line in IN:
    d, val, color = line.split()
    color = color[2:-1]
    d = color[-1:]
    val = int(color[:-1], 16)

    point = (current[0] + val * DIRS[d][0], current[1] + val * DIRS[d][1])
    points.append(point)
    current = point


def shoelace(points):
    n = len(points)
    area = 0.0
    perimeter = 0.0
    for i in range(n):
        prev = points[i]
        next_ = points[(i + 1) % n]
        area += prev[1] * next_[0]
        area -= prev[0] * next_[1]
        perimeter += abs(prev[0] - next_[0]) + abs(prev[1] - next_[1])
    return int((abs(area) / 2.0) + (perimeter / 2.0) + 1)


print(shoelace(points))
