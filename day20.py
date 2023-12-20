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


def send_pulse(name):
    queue = deque([(name, False, "button")])
    high_count = 0
    low_count = 0
    while queue:
        current_name, current_high, current_caller = queue.popleft()
        if current_high:
            high_count += 1
        else:
            low_count += 1
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
    return high_count, low_count


high, low = 0, 0
for i in range(1000):
    h, l = send_pulse("broadcaster")
    high += h
    low += l
print(f"part1: {high * low}")
