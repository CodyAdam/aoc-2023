IN = open("in.txt").read().splitlines()

grid = [list(line) for line in IN]

points = set()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            points.add((x, y))


def show_grid(points):
    min_x = min([x for x, _ in points])
    max_x = max([x for x, _ in points])
    min_y = min([y for _, y in points])
    max_y = max([y for _, y in points])

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x, y) in points:
                print("# ", end="")
            else:
                print(". ", end="")
        print()
    print("---")


def shift_right(after_x, amount):
    global points
    new_points = set()
    for x, y in points:
        if x >= after_x:
            new_points.add((x+amount, y))
        else:
            new_points.add((x, y))
    return new_points


def shift_down(points, after_y, amount):
    new_points = set()
    for x, y in points:
        if y >= after_y:
            new_points.add((x, y+amount))
        else:
            new_points.add((x, y))
    return new_points


# show_grid(points)
for y in range(len(grid)-1, -1, -1):
    # if empty row, shift down
    if "#" not in grid[y]:
        points = shift_down(points, y, 1000000-1)

for x in range(len(grid[0])-1, -1, -1):
    # if empty column, shift right
    if "#" not in [row[x] for row in grid]:
        points = shift_right(x, 1000000-1)

# show_grid(points)


print(points)


from itertools import combinations

def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

sum_dist = 0
for p1,p2 in combinations(points, 2):
    dist = manhattan(p1, p2)
    sum_dist += dist 
print(sum_dist)

