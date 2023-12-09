import math


IN = open("in.txt").read().splitlines()

INSTRUCTIONS = list(map(lambda x: 1 if x == "R" else 0, IN[0].strip()))

graph: dict[str, list[str]] = {}

for line in IN[2:]:
    # AAA = (BBB, CCC)
    node, childs = line.split(" = ")
    left, right = childs[1:-1].split(", ")
    graph[node] = [left, right]


def get_next(node, i):
    return graph[node][INSTRUCTIONS[i % len(INSTRUCTIONS)]]


def get_end(node):
    i = 0
    while True:
        if node.endswith("Z"):
            return i
        node = get_next(node, i % len(INSTRUCTIONS))
        i += 1


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_list(l: list[int]):
    if len(l) == 1:
        return l[0]
    return lcm(l[0], lcm_list(l[1:]))

starts = []
for key in graph.keys():
    if key.endswith("A"):
        starts.append(key)


lcms = []
for start in starts:
    lcms.append(get_end(start))

print(lcms)
print(lcm_list(lcms))
