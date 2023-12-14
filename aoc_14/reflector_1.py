# Answer: 109939

import numpy as np


def move_rock(x, y, data):

    y_lim = y
    # while we do not hit a wall or a #
    while (y_lim-1 >= 0) and (data[y_lim - 1, x] not in ["O", "#"]):
        y_lim -= 1
    if y_lim != y:
        data[y_lim, x] = "O"
        data[y, x] = "."
    load = len(data) - y_lim
    return data, load


if __name__ == '__main__':
    with open("input.txt") as f:
        data = f.read().splitlines()
    data = np.array([list(line) for line in data])

    (len_y, len_x) = np.shape(data)
    total_load = 0

    for y in range(len_y):
        for x in range(len_x):
            if data[y][x] == "O":
                data, load = move_rock(x, y, data)
                total_load += load
    print(total_load)
