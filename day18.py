IN = open("in.txt").read().splitlines()
DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

min_x = 0
max_x = 0
min_y = 0
max_y = 0
current = (0, 0)
walls = set([current])
for line in IN:
    d, val, color = line.split()
    color = color[1:-1]
    val = eval(val)
    for _ in range(val):
        current = tuple(map(sum, zip(current, DIRS[d])))
        if current[0] < min_x:
            min_x = current[0]
        if current[0] > max_x:
            max_x = current[0]
        if current[1] < min_y:
            min_y = current[1]
        if current[1] > max_y:
            max_y = current[1]
        walls.add(current)


def bfs(pos, walls):
    if pos in walls:
        return set()
    queue = [pos]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        for d in DIRS.values():
            new = tuple(map(sum, zip(current, d)))
            if min_x > new[0] or max_x < new[0] or min_y > new[1] or max_y < new[1]:
                return set()
            if new not in walls:
                queue.append(new)
    return visited


inside = bfs((2, 1), walls)
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) in walls or (x, y) in inside:
            print("#", end="")
        else:
            print(".", end="")
    print()
print(len(inside), len(walls))
print(len(inside) + len(walls))
