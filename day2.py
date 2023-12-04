import re
s = 0
lines = open("in.txt").read().splitlines()

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

s = 0

target = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for game in lines:
    game_id, sub_game = game.split(": ")
    game_id = int(game_id.split(" ")[1])
    sub_game = sub_game.split("; ")
    sub_game = [ball.split(", ") for ball in sub_game]

    max_colors = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for balls in sub_game:
        for b in balls:
            count, color = b.split()
            count = int(count)
            max_colors[color] = max(max_colors[color], count)

    s+= max_colors["red"] * max_colors["green"] * max_colors["blue"]
    # if max_colors["red"] <= target["red"] and max_colors["green"] <= target["green"] and max_colors["blue"] <= target["blue"]:
    #     s += game_id

print(s)
