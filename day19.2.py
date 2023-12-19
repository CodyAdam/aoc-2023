RULES, PARTS = open("in.txt").read().split("\n\n")

RULES = RULES.splitlines()
PARTS = PARTS.splitlines()

rules = {}
for rule in RULES:
    label, ifs = rule[:-1].split("{")
    ifs = ifs.split(",")
    rules_list = []
    for if_ in ifs:
        if ":" in if_:
            cond, out = if_.split(":")
            rules_list.append((cond, out))
        else:
            out = if_
            rules_list.append(("True", out))
    rules[label] = rules_list

VAR_IDX = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3,
}

def get_new_range(cond, part_range):
    if "<" in cond:
        var, value = cond.split("<")
        value = int(value)
        var_idx = VAR_IDX[var]

        true_range = list(part_range)
        true_range[var_idx] = (part_range[var_idx][0], value - 1)
        false_range = list(part_range)
        false_range[var_idx] = (value, part_range[var_idx][1])
        return true_range, false_range
    elif ">" in cond:
        var, value = cond.split(">")
        value = int(value)
        var_idx = VAR_IDX[var]

        true_range = list(part_range)
        true_range[var_idx] = (value + 1, part_range[var_idx][1])
        false_range = list(part_range)
        false_range[var_idx] = (part_range[var_idx][0], value)
        return true_range, false_range
    else:
        raise Exception("Invalid condition", cond)


def get_combi(label, part_range):
    if label == "R":
        return 0
    if label == "A":
        x, m, a, s = part_range
        return (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
    x, m, a, s = part_range
    ans = 0
    print(label, part_range)
    for condition, out in rules[label]:
        if condition == "True":
            ans += get_combi(out, part_range)
            continue
        true_range, false_range = get_new_range(condition, part_range)
        ans += get_combi(out, true_range)
        part_range = false_range
    return ans


print(get_combi("in", ((1, 4000), (1, 4000), (1, 4000), (1, 4000))))
