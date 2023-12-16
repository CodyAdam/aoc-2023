grid = open("in.txt").read().splitlines()

mirrors = {}

H = len(grid)
W = len(grid[0])

for y in range(H):
    for x in range(W):
        cell = grid[y][x]
        if cell != ".":
            mirrors[(x, y)] = cell


def is_inbound(pos):
    x, y = pos
    if x < 0 or y < 0 or x >= W or y >= H:
        return False
    return True


def get_new_dirs(prev_dir, mirror):
    if mirror == "-" and (prev_dir == (0, 1) or prev_dir == (0, -1)):
        return [(1, 0), (-1, 0)]
    if mirror == "|" and (prev_dir == (-1, 0) or prev_dir == (1, 0)):
        return [(0, 1), (0, -1)]
    if mirror == "/" and prev_dir == (0, -1):
        return [(1, 0)]
    if mirror == "/" and prev_dir == (0, 1):
        return [(-1, 0)]
    if mirror == "/" and prev_dir == (1, 0):
        return [(0, -1)]
    if mirror == "/" and prev_dir == (-1, 0):
        return [(0, 1)]
    if mirror == "\\" and prev_dir == (0, -1):
        return [(-1, 0)]
    if mirror == "\\" and prev_dir == (0, 1):
        return [(1, 0)]
    if mirror == "\\" and prev_dir == (1, 0):
        return [(0, 1)]
    if mirror == "\\" and prev_dir == (-1, 0):
        return [(0, -1)]
    return [prev_dir]


def show(current=None):
    global visited, grid, H, W
    vis = set()
    if not current:
        for v in visited:
            vis.add((v[0], v[1]))
    else:
        vis.add(current)
    print()
    for y in range(H):
        for x in range(W):
            if (x, y) in vis:
                print("#", end="")
            elif (x, y) in mirrors:
                print(mirrors[(x, y)], end="")
            else:
                print(".", end="")
        print()


def get_starts(H, W):
    starts = []
    for y in range(H):
        starts.append((-1, y, (1, 0)))
        starts.append((W, y, (-1, 0)))
    for x in range(W):
        starts.append((x, -1, (0, 1)))
        starts.append((x, H, (0, -1)))
    return starts

out = []
for start in get_starts(H,W):
    rays = [start]
    visited = set()

    while len(rays):
        x, y, direction = rays.pop()
        # show((x, y))
        # print((x, y, direction))
        dx, dy = direction

        nx, ny = x + dx, y + dy
        if not is_inbound((nx, ny)):
            continue
        new_dirs = [direction]
        if (nx, ny) in mirrors:
            new_dirs = get_new_dirs(direction, mirrors[(nx, ny)])
        for d in new_dirs:
            node = (nx, ny, d)
            if node not in visited:
                visited.add(node)
                rays.append(node)
        # input()

    vis = set()
    for v in visited:
        vis.add((v[0], v[1]))
    number = len(vis)
    out.append(number)
print(max(out))