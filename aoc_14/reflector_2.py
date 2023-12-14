# Answer: 101010

import numpy as np
from tqdm import tqdm


def total_load(data):
    total_load = 0
    (len_y, len_x) = np.shape(data)
    for y in range(len_y):
        for x in range(len_x):
            if data[y][x] == "O":
                total_load += len(data) - y
    return total_load


def move_rock(x, y, data):
    y_lim = y
    # while we do not hit a wall or a #
    while (y_lim-1 >= 0) and (data[y_lim - 1, x] not in ["O", "#"]):
        y_lim -= 1
    if y_lim != y:
        data[y_lim, x] = "O"
        data[y, x] = "."
    return data


if __name__ == '__main__':
    # At some point there is a periodicity after 44 cycles the data is the same again
    # Cycle 1.000.000.000 should be the same as cycle 1.000.000.000 - 44 * n
    # E.g. cycle 32, 76, 120, 164
    with open("input.txt") as f:
        data = f.read().splitlines()
    data = np.array([list(line) for line in data])
    (len_y, len_x) = np.shape(data)

    history = []
    history.append(data.copy())

    cycle = False

    # while not cycle:
    for cycle in tqdm(range(1, 1000)):
        for i in enumerate(['N', 'W', 'S', 'E']):
            for y in range(len_y):
                for x in range(len_x):
                    if data[y][x] == "O":
                        data = move_rock(x, y, data)
            data = np.rot90(data, 3)
        if cycle >= 164 and (cycle-164) % 44 == 0:
            print(f"Cycle {cycle} is done: Total load {total_load(data)}")
        # print(data, "\n")
        # for h, data_h in enumerate(history):
        #     if np.array_equal(data, data_h):
        #         print(data)
        #         print(data_h)
        #         print(f"Data of iteration {n} is equal to historical data at iteration {h}")
        #         # cycle = True
        # else:
        #     history.append(data.copy())
