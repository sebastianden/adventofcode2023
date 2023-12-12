# Answers
# 2.2: 62241

with open('input.txt') as f:
    # Read lines wihout newline character
    lines = [line.rstrip() for line in f]

dict_list = []
for line in lines:
    game_map = {
        "red": 1,
        "green": 1,
        "blue": 1,
    }
    for round in line.split(':')[1].split(';'):
        for color in round.split(','):
            # Find out which color it is
            for c in game_map.keys():
                if c in color:
                    n_dice = int(color.split(' ')[1])
                    if n_dice > game_map[c]:
                        game_map[c] = n_dice
    dict_list.append(game_map)

power_list = []
for game_map in dict_list:
    power_list.append(game_map["red"] * game_map["green"] * game_map["blue"])

print(sum(power_list))
