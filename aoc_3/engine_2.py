# Answer: 91031374

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

max_x = len(lines[0])
max_y = len(lines)
symbols = ['*', '/', '$', '+', '&', '@', '#', '%', '=', '-']


def get_whole_number(lines, i, j):
    whole_number_list = []
    # Go left until we find a symbol
    while lines[j][i-1].isdigit() and i > 0:
        i -= 1

    # Go right adding digits to list until we find a symbol
    while i < max_x and lines[j][i].isdigit():
        whole_number_list.append(lines[j][i])
        i += 1

    return int(''.join(whole_number_list))


def walk_around_star(lines, i, j):
    number_list = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < max_x and y >= 0 and y < max_y:
                if lines[y][x].isdigit():
                    number_list.append(get_whole_number(lines, x, y))
    return number_list

    # Walk around the "*" and look for digits
    # If one is found get the whole number and add it to the whole numbers list
    # Once we are around the "*" deduplicate the whole numbers list and only leave unique numbers (this might be a wrong assumption!)
    # If there are 2 unique numbers, multiply them and add them to the gear list
    # If yes, multiply them and add them to the list


if __name__ == "__main__":

    gear_list = []
    # Go through list until we find a "*"
    for j in range(max_y):
        for i in range(max_x):
            element = lines[j][i]
            if element == '*':
                number_list = walk_around_star(lines, i, j)
                if len(set(number_list)) == 2:
                    unique_number_list = set(number_list)
                    gear_list.append(
                        unique_number_list.pop() * unique_number_list.pop())
    print(sum(gear_list))
