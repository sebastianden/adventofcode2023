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


def run_cycle(data):
    (len_y, len_x) = np.shape(data)
    for _ in ['N', 'W', 'S', 'E']:
        for y in range(len_y):
            for x in range(len_x):
                if data[y][x] == "O":
                    data = move_rock(x, y, data)
        data = np.rot90(data, 3)
    return data


if __name__ == '__main__':
    # Find the periodicity (number of cycles after which the output is the same
    # again). Cycle 1.000.000.000 should be the same as cycle
    # 1.000.000.000 - 44 * n as long as the cycle is larger than the max size of
    # the data --> In this specific case cycle 120 is the first where the cycle
    # repeats and which is a multiple of 44 away from 1e9

    rep = 1e9

    with open("input.txt") as f:
        data = f.read().splitlines()
    data = np.array([list(line) for line in data])

    start_data = data.copy()

    (len_y, len_x) = np.shape(data)

    # Find the periodicity in the cycles by comparing the output of cycle
    # len(data) with the output of the following cycles, if it's the same we
    # have a periodicity
    cycle = False
    n = 0
    compare_data = None
    while not cycle:
        n += 1
        data = run_cycle(data)
        if n == np.max(np.shape(data)):
            compare_data = data.copy()
        elif n >= np.max(np.shape(data)) and np.array_equal(data, compare_data):
            p = n - np.max(np.shape(data))
            print(f"Cycle {n} is the same as cycle {np.max(np.shape(data))}. Periodicity found p = {p}.")
            cycle = True

    # Get the first cycle that has the same output as cycle 1e9
    min_cycle = int(rep % p)
    while min_cycle < np.max(np.shape(data)):
        min_cycle += p

    # Reset data to the initial state
    data = start_data.copy()
    # Run the cycles
    for cycle in tqdm(range(0, min_cycle)):
        data = run_cycle(data)
    print(total_load(data))
