# Answer: 546563

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

unique_symbols = ['*', '/', '$', '+', '&', '@', '#', '%', '=', '-']

# x and y are switched but it doesn't matter because the input was quadratic
max_x = len(lines[0])
max_y = len(lines)


def is_adjacent_to_symbol(lines, i, j):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < max_x and y >= 0 and y < max_y:
                if lines[x][y] in unique_symbols:
                    return True
    return False


number_list = []
digit_list = []
adjacent_list = []

for i in range(max_x):
    for j in range(max_y):
        element = lines[i][j]
        if element.isdigit():
            digit_list.append(element)
            adjacent_list.append(is_adjacent_to_symbol(lines, i, j))
        if (element == '.' or element in unique_symbols) and digit_list:
            if any(adjacent_list):
                number_list.append(int(''.join(digit_list)))
            # Reset digit_list and adjacent_list
            digit_list, adjacent_list = [], []
print(sum(number_list))
