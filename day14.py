
grid = open("in.txt").read().splitlines()

H = len(grid)
W = len(grid[0])

walls = set()
rocks = set()



def show():
    global walls, rocks, grid
    print()
    for y in range(H):
        for x in range(W):
            if (x, y) in rocks:
                print("O", end="")
            elif (x, y) in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()


for y in range(H):
    for x in range(W):
        if grid[y][x] == "#":
            walls.add((x, y))
        elif grid[y][x] == "O":
            rocks.add((x, y))


def to_dir(rock_pos, direction):
    global walls, rocks, W, H
    x, y = rock_pos
    dx, dy = direction
    curY = y + dy
    curX = x + dx
    while curY >= 0 and curX >= 0 and curY < H and curX < W:
        if (curX, curY) in walls or (curX, curY) in rocks:
            return (curX-dx, curY-dy)
        curY += dy
        curX += dx
    return (curX-dx, curY-dy)


def score():
    global rocks
    s = 0
    for x, y in rocks:
        s += H - y
    return s


def move_top():
    for y in range(H):
        for x in range(W):
            if (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add(to_dir((x, y), (0, -1)))


def move_left():
    for x in range(W):
        for y in range(H):
            if (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add(to_dir((x, y), (-1, 0)))


def move_right():
    for x in range(W-1, -1, -1):
        for y in range(H):
            if (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add(to_dir((x, y), (1, 0)))


def move_bottom():
    for y in range(H-1, -1, -1):
        for x in range(W):
            if (x, y) in rocks:
                rocks.remove((x, y))
                rocks.add(to_dir((x, y), (0, 1)))


cache = []

i = 0
MAX = 1000000000
while i < MAX:
    move_top()
    move_left()
    move_bottom()
    move_right()

    hashed = hash(frozenset(rocks))
    print(hashed)
    if hashed in cache:
        print("found loop")
        loop_length = i - cache.index(hashed)
        remaining = MAX - i
        remaining %= loop_length
        i = MAX - remaining
        cache = []
    cache.append(hashed)
    i += 1
show()
print(i)
print(score())


