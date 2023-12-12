# Answer: 790194712336

from math import factorial
import numpy as np


def expand(sky_map, n):
    counter = 0
    # Find all rows only containing '.'
    empty_rows = np.where(np.all(sky_map == '.', axis=1))[0]
    y_index = np.zeros(len(sky_map))
    for y in range(len(sky_map)):
        if y in empty_rows:
            counter += n
        else:
            counter += 1
        y_index[y] += counter

    counter = 0
    # Find all columns only containing '.'
    empty_cols = np.where(np.all(sky_map == '.', axis=0))[0]
    x_index = np.zeros(len(sky_map[0]))
    for x in range(len(sky_map[0])):
        if x in empty_cols:
            counter += n
        else:
            counter += 1
        x_index[x] += counter

    print("Empty rows: ", empty_rows)
    print("Empty columns: ", empty_cols)

    return x_index, y_index


def count_galaxies(sky_map):
    count = 1
    numbered_map = np.zeros(sky_map.shape)
    for y in range(sky_map.shape[0]):
        for x in range(sky_map.shape[1]):
            if sky_map[y, x] == '#':
                numbered_map[y, x] = count
                count += 1
            else:
                numbered_map[y, x] = 0

    return numbered_map


def generate_unique_pairs(n):
    return [(i, j) for i in range(1, n) for j in range(i+1, n+1)]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    expansion_factor = 1e6

    # Read input
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    sky_map = np.array([list(line) for line in data])
    print(sky_map)

    x_index, y_index = expand(sky_map, expansion_factor)

    print(x_index, y_index)

    numbered_map = count_galaxies(sky_map)

    print(numbered_map)

    print("Possible combinations: ", factorial(int(np.max(numbered_map)))/(2*factorial(int(np.max(numbered_map)) - 2)))

    # Get all possible pairs of galaxies
    pairs = generate_unique_pairs(int(np.max(numbered_map)))
    # print(pairs)
    print(len(pairs))

    total_distance = 0
    for pair in pairs:
        A = np.where(numbered_map == pair[0])
        B = np.where(numbered_map == pair[1])
        A_converted = (y_index[A[0][0]], x_index[A[1][0]])
        B_converted = (y_index[B[0][0]], x_index[B[1][0]])
        total_distance += manhattan_distance(A_converted, B_converted)

    print(total_distance)
