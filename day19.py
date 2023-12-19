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


def get_out(label, part):
    if label in "AR":
        return label
    x, m, a, s = part
    for condition, out in rules[label]:
        if eval(condition) == True:
            return get_out(out, (x, m, a, s))
    raise Exception("No rule found for label", label)


ans = 0
for raw_part in PARTS:
    x, m, a, s = raw_part[1:-1].split(",")
    part = (int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:]))
    out = get_out("in", part)
    if out == "A":
        ans += sum(part)
print(ans)