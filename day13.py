IN = open("in.txt").read().split("\n\n")

s = 0


def is_sym_vert(grid, mirror_x):
    H = len(grid)
    W = len(grid[0])
    off_count = 0
    for y in range(H):
        for x in range(mirror_x):
            mirrored_x = 2*mirror_x - x-1
            if mirrored_x >= W:
                continue
            if grid[y][x] != grid[y][mirrored_x]:
                off_count += 1
    return off_count


def is_sym_hor(grid, mirror_y):
    H = len(grid)
    W = len(grid[0])
    off_count = 0
    for y in range(mirror_y):
        for x in range(W):
            mirrored_y = 2*mirror_y - y-1
            if mirrored_y >= H:
                continue
            if grid[y][x] != grid[mirrored_y][x]:
                off_count += 1
    return off_count


def show(grid):
    print()
    for line in grid:
        print(line)


s = 0
for puzzle in IN:
    grid = puzzle.splitlines()
    H = len(grid)
    W = len(grid[0])
    show(grid)
    for y in range(1, H):
        if is_sym_hor(grid, y) == 1:
            s += y * 100
            print("-", y)

    for x in range(1, W):
        if is_sym_vert(grid, x) == 1:
            s += x
            print("|", x)
print(s)
