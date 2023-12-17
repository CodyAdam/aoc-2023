import heapq

grid = open("in.txt").read().splitlines()


def valid(pos):
    return 0 <= pos[0] < W and 0 <= pos[1] < H


def is_oposite(d1, d2):
    return d1[0] == -d2[0] and d1[1] == -d2[1]


H = len(grid)
W = len(grid[0])
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
START = (0, 0)
END = (W-1, H-1)
q = []
visited = {
    (START, (1, 0), 0): 0
}

heapq.heappush(q, (0, (START, (1, 0), 0)))

while q:
    _, node = heapq.heappop(q)
    pos, prev_dir, occur = node
    for dire in DIRS:
        if occur < 4 and dire != prev_dir:
            continue
        new_pos = (pos[0]+dire[0], pos[1]+dire[1])
        new_occur = occur + 1 if dire == prev_dir else 1
        if new_occur > 10 or not valid(new_pos) or is_oposite(dire, prev_dir):
            continue
        new_val = int(grid[new_pos[1]][new_pos[0]]) + visited[node]
        new_node = (new_pos, dire, new_occur)
        if new_node not in visited or new_val < visited[new_node]:
            visited[new_node] = new_val
            heapq.heappush(q, (new_val, new_node))

# Find the value of the END node
for node in visited:
    if node[0] == END:
        print(visited[node])
        break