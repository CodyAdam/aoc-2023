IN = open("in.txt", "r").read().splitlines()
wins = []
for game in IN:
    found = 0
    left, right = game.split(": ")[1].split(" | ")
    winning = left.split()
    mine = right.split()
    for c in mine:
        if c in winning:
            found += 1
    wins.append(found)

wins.reverse()
count = [1] * len(wins)
for i, val in enumerate(wins):
    for j in range(val):
        count[i] += count[i - j - 1]

print(sum(count))
