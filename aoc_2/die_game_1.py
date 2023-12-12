# Answers
# 2.1: 2207

max_dice = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_game_possible(line):
    for round in line.split(':')[1].split(';'):
        for color in round.split(','):
            # Find out which color it is
            for c in max_dice.keys():
                if c in color:
                    n_dice = int(color.split(' ')[1])
                    if max_dice[c] < n_dice:
                        return False
    return True


with open('input.txt') as f:
    # Read lines wihout newline character
    lines = [line.rstrip() for line in f]

sum = 0
for i, line in enumerate(lines):
    if is_game_possible(line):
        sum += i+1

print(sum)
