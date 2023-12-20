from collections import defaultdict, deque


IN = open("in.txt").read().splitlines()

flips = defaultdict(bool)
conjunctions = {}
nodes = {}

for line in IN:
    name, outs = line.split(" -> ")
    outs = outs.split(", ")
    if name.startswith("%"):
        name = name[1:]
        flips[name] = False
    elif name.startswith("&"):
        name = name[1:]
        conjunctions[name] = {}
    nodes[name] = outs

# Setup conjunctions inputs
for name in conjunctions:
    for other_name, outs in nodes.items():
        for out in outs:
            if out == name:
                conjunctions[name][other_name] = False
                break


def send_pulse(name, to_watch=[]):
    queue = deque([(name, False, "button")])
    watch_count = [0] * len(to_watch)
    while queue:
        current_name, current_high, current_caller = queue.popleft()
        if current_name in to_watch and not current_high:
            watch_count[to_watch.index(current_name)] += 1
        # print(f"{current_caller} -{'high' if current_high else 'low'}-> {current_name}")
        if current_name in flips:
            if current_high:
                continue
            flips[current_name] = not flips[current_name]
            for out in nodes[current_name]:
                queue.append((out, flips[current_name], current_name))

        elif current_name in conjunctions:
            if current_caller == "button":
                raise Exception("Conjunctions cannot be called directly")
            conjunctions[current_name][current_caller] = current_high
            if all(conjunctions[current_name].values()):
                for out in nodes[current_name]:
                    queue.append((out, False, current_name))
            else:
                for out in nodes[current_name]:
                    queue.append((out, True, current_name))

        elif current_name in nodes:
            for out in nodes[current_name]:
                queue.append((out, current_high, current_name))
    return watch_count


rx_parent = None
for n in nodes:
    if "rx" in nodes[n]:
        rx_parent = n
        break

rx_parent_parent = []
for n in nodes:
    if rx_parent in nodes[n]:
        rx_parent_parent.append(n)

i = 1
parent_index = [0] * len(rx_parent_parent)
while 0 in parent_index:
    watched = send_pulse("broadcaster", rx_parent_parent)
    if sum(watched) > 0:
        print(i, [rx_parent_parent[index] for index, count in enumerate(watched) if count > 0])
        for index, count in enumerate(watched):
            if count > 0 and parent_index[index] == 0:
                parent_index[index] = i
    i += 1


def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_list(l):
    value = l[0]
    for i in l[1:]:
        value = lcm(value, i)
    return value

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(parent_index)
print(lcm_list(parent_index))
