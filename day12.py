from functools import cache

IN = open("in.txt").read().splitlines()


@cache
def count(sequence, rules):
    if not rules:
        return 0 if "#" in sequence else 1
    if not sequence:
        return 1 if not rules else 0

    result = 0

    if sequence[0] in ".?": # IGNORE
        result += count(sequence[1:], rules)
    if sequence[0] in "#?": # TAKE
        if (
            rules[0] <= len(sequence)
            and "." not in sequence[: rules[0]]
            and (rules[0] == len(sequence) or sequence[rules[0]] != "#")
        ):
            result += count(sequence[rules[0] + 1:], rules[1:])

    return result


s = 0
for line in IN:
    sequence, rules = line.split()
    rules = tuple(map(int, rules.split(","))) * 5
    sequence = "?".join([sequence] * 5)
    s += count(sequence, rules)

print(s)
