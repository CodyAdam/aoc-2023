from collections import defaultdict
from functools import cache


IN = open("in.txt").read().splitlines()

W = len(IN[0])
H = len(IN)
chunks = defaultdict(set)
walls = set()


for y in range(len(IN)):
    for x in range(len(IN[y])):
        cell = IN[y][x]
        if cell == "#":
            walls.add((x, y))
        elif cell == "S":
            chunks[(0, 0)].add((x, y))


def show():
    print()
    points = chunks[(0, 0)]
    for y in range(H):
        for x in range(W):
            if (x, y) in walls:
                print("██", end="")
            elif (x, y) in points:
                print("O ", end="")
            else:
                print("░░", end="")
        print()
    print(len(points))


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


@cache
def step(points):
    new_points = set()
    for x, y in points:
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in walls:
                continue
            new_points.add((nx, ny))
    return new_points


looping_chunks = set()
chunks_history = defaultdict(list)
waiting_points = defaultdict(set)


def get_outbound_points(points):
    outbound_points = set()
    cleaned_points = set()
    for x, y in points:
        if x < 0:
            outbound_points.add(((-1, 0), (x % W, y)))
        elif x >= W:
            outbound_points.add(((1, 0), (x % W, y)))
        elif y < 0:
            outbound_points.add(((0, -1), (x, y % H)))
        elif y >= H:
            outbound_points.add(((0, 1), (x, y % H)))
        else:
            cleaned_points.add((x, y))
    return cleaned_points, outbound_points


show()
for i in range(1000):
    for chunk in chunks.keys() | waiting_points.keys():
        if chunk in looping_chunks:
            loop_length = len(
                chunks_history[chunk]) - chunks_history[chunk].index(chunks[chunk])
            # print("looping chunk", chunk, loop_length)
            continue
        points = step(tuple(chunks[chunk])) | waiting_points[chunk]
        waiting_points[chunk] = set()
        points, outbound_points = get_outbound_points(points)
        for chunk_offset, outbound in outbound_points:
            dx, dy = chunk_offset
            cx, cy = chunk
            new_chunk = (cx + dx, cy + dy)
            waiting_points[new_chunk].add(outbound)

        chunks[chunk] = points
        if chunks[chunk] in chunks_history[chunk]:
            looping_chunks.add(chunk)
        chunks_history[chunk].append(chunks[chunk])
    # for k in chunks:
    #     print(k)
    #     print("    ", chunks[k])
    # input()
print(sum(len(chunks[k]) for k in chunks))
