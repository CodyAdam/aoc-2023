grid = open("in.txt").read().splitlines()
grid = [list(line) for line in grid]

H = len(grid)
W = len(grid[0])

DIR = {
    ".": [],
    "-": [(1, 0), (-1, 0)],
    "|": [(0, 1), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "L": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def get_opposite_dir(pos):
    x, y = pos
    return (-x, -y)




def get_dir(pos):
    global H, W
    x, y = pos
    dirs = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue
        dirs.append((dx, dy))
    cell = grid[y][x]
    options = set(DIR[cell])

    return set(dirs) & options


def get_posibilities(pos):
    posibilities = []
    x, y = pos
    for dx, dy in get_dir(pos):
        nx, ny = x + dx, y + dy
        if pos in [(nx+px, ny+py) for px, py in get_dir((nx, ny))]:
            posibilities.append((dx, dy))
    return posibilities

START = None
for y in range(H):
    for x in range(W):
        if START:
            break
        if grid[y][x] == "S":
            START = (x, y)


visited = set()
current = START
i = 0
loop_tiles = set([current])
while current not in visited:
    visited.add(current)
    possibles = get_posibilities(current)
    for (dx,dy) in possibles:
        new_pos = (current[0] + dx, current[1] + dy)
        if new_pos not in visited:
            current = new_pos
            break
    loop_tiles.add(current)
    i += 1

print(i//2)

# part 2 ------------------------------

# remove any non-loop tiles
for y in range(H):
    for x in range(W):
        if (x, y) not in loop_tiles:
            grid[y][x] = "."

for line in grid:
    print("".join(line))


def get_neigh(pos):
    global H, W
    x, y = pos
    dirs = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue
        dirs.append((dx, dy))
    return dirs

def bfs(start):
    visited = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        neighbours = get_neigh(current)
        for dx, dy in neighbours:
            nx, ny = current[0] + dx, current[1] + dy
            if is_inbound((nx, ny)) and (nx, ny) not in visited and grid[ny][nx] == ".":
                queue.append((nx, ny))
    return visited

def get_left(move):
    # do a 90 degree left rotation
    x, y = move
    if x == 0:
        if y == 1:
            return (-1, 0)
        else:
            return (1, 0)
    else:
        if x == 1:
            return (0, 1)
        else:
            return (0, -1)
def get_right(move):
    # do a 90 degree right rotation
    x, y = move
    if x == 0:
        if y == 1:
            return (1, 0)
        else:
            return (-1, 0)
    else:
        if x == 1:
            return (0, -1)
        else:
            return (0, 1)
        
def is_inbound(pos):
    global H, W
    x, y = pos
    return x >= 0 and y >= 0 and x < W and y < H

visited = set()
current = START
empty_visited = set()
while current not in visited:
    visited.add(current)
    possibles = get_posibilities(current)
    for (px, py) in possibles:
        new_pos = (current[0] + px, current[1] + py)
        if new_pos not in visited:
            left = get_left((px, py))
            left_pos = (current[0] + left[0], current[1] + left[1])
            if is_inbound(left_pos):
                left_cell = grid[left_pos[1]][left_pos[0]]
                if left_cell == ".":
                    empty_visited = empty_visited | bfs(left_pos)
            else:
                print("OOB")
                exit()
            left_left_pos = (new_pos[0] + left[0], new_pos[1] + left[1])
            if is_inbound(left_left_pos):
                left_left_cell = grid[left_left_pos[1]][left_left_pos[0]]
                if left_left_cell == ".":
                    empty_visited = empty_visited | bfs(left_left_pos)
            else:
                print("OOB")
                exit()
            current = new_pos
            break

print(len(empty_visited))
