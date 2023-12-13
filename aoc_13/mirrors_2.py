# Answer: 30487

import numpy as np


def get_mirror_count(m, axis=0, n_diff=0):

    ax_len = np.shape(m)[axis]
    if axis == 1:
        m = np.transpose(m)
    # Find two lines next to each other that are the same or have exactly one difference
    for i in range(ax_len-1):
        if np.sum(m[i] != m[i+1]) <= n_diff:
            print(f"Index {i}")
            # Verify that the center is found
            min_side = min(i, ax_len - i - 2)
            # Go left and right from the index until one side is reached and check that the lines are the same
            differences = 0
            for j in range(0, min_side + 1):
                # print(m[index - j])
                # print(m[index + j + 1])
                differences += np.sum(m[i - j] != m[i + j + 1])
                if differences > n_diff:
                    break
            if differences == n_diff:
                return i + 1
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()

    single_map = []
    map_list = []
    for line in data:
        if line != '':
            single_map.append(list(line))
        else:
            map_list.append(np.array(single_map))
            single_map = []
    map_list.append(np.array(single_map))

    count = 0
    for m in map_list:
        print(m)
        count += get_mirror_count(m, axis=1, n_diff=1)
        count += 100 * get_mirror_count(m, axis=0, n_diff=1)
    print(count)
